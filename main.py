import openai
import speech_recognition as sr
import pyttsx3;

# Init text to speech, voice recognition and mic input
engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()

# Set Key
openAIKey = ""

# Set up the OpenAI API client
openai.api_key = openAIKey

# Get user's prompt
with mic as source:
    print("listening")
    audio = r.listen(source)

# Get user speech as a string
speech = r.recognize_google(audio)

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = speech

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

# Output response through text-to-speech audio
engine.say(response)
engine.runAndWait()