# speech.py
import pyttsx3
import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "I couldn't understand that."
    except sr.RequestError:
        return "There was an error with the speech recognition service."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
