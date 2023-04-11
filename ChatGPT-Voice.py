import openai
import pyttsx3
import speech_recognition as sr
import time

# set OpenAI API key
openai.api_key = "Insert-API-Key"

# text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Skipping unknown error")
