import os
import openai
import speech_recognition as sr
import pyttsx3;

# Init text to speech, voice recognition and mic input
engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()

# Set Key
openAIKey = "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"

# Record previous context, with each elemeant being a dictionary, where teh key is the prompt and the value the answer
conetext = []

# Set up the OpenAI API client
openai.api_key = openAIKey

# Get user's prompt
while True:
    with mic as source:
        input("Press any key")
        print("listening")
        audio = r.listen(source)

    # Get user speech as a string
    speech = r.recognize_google(audio)

    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = speech

    # If there has been previous answers, add the context to the promt
    if len(conetext) != 0:
        addedContext = "In order, I previously asked you these questions and you gave me these answers: "
        for el in conetext:
            key, value = list(el.items())[0]
            addedContext += "Question, " + key + " Your answer: " + value
        addedContext += ". Now my new quetion is this: "
        prompt = addedContext + prompt

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get openAI response
    response = completion.choices[0].text
    print(response)

    # Track context
    conetext.append({prompt : response})

    # Output response through text-to-speech audio
    engine.say(response)
    engine.runAndWait()