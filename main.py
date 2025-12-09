import os
import time
import subprocess
import speech_recognition as sr
import pygame
from gtts import gTTS
from groq import Groq
from dotenv import load_dotenv

load_dotenv() 

# Get the key securely
# INSTRUCTIONS FOR GITHUB USERS:
# 1. Create a file named .env in the project root
# 2. Add this line inside: GROQ_API_KEY=your_groq_api_key_here

API_KEY = os.getenv("GROQ_API_KEY") 

if not API_KEY:
    raise ValueError("API Key not found! Please check your .env file.")

client = Groq(api_key=API_KEY)

pygame.mixer.init()

def speak(text):
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        filename = "temp_voice.mp3"
        tts.save(filename)
        
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
    except Exception as e:
        print(f"Error in speaking: {e}")

def take_command():
    print("\nListening... (Speak now)")
    
    try:
        subprocess.call(["arecord", "-f", "cd", "-d", "4", "-r", "16000", "-q", "input.wav"])
        
        print("Recognizing...")
        recognizer = sr.Recognizer()
        
        with sr.AudioFile("input.wav") as source:
            audio_data = recognizer.record(source)
            
        query = recognizer.recognize_google(audio_data)
        print(f"User said: {query}")
        return query

    except Exception:
        return None

def get_ai_response(query):
    try:
        print("AI is thinking...")
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant named Jarvis. Answer in 1 or 2 sentences."
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            model="llama-3.1-8b-instant",
            temperature=1,
        )
        return chat_completion.choices[0].message.content
        
    except Exception:
        return "Sorry, I am having trouble connecting to the server."

def run_assistant():
    print("--- JARVIS STARTED ---")
    speak("I am online. How can I help you?")

    while True:
        query = take_command()
        
        if query:
            query = query.lower()
            
            if 'stop' in query or 'exit' in query or 'quit' in query:
                print("Stopping program...")
                speak("Goodbye, sir.")
                break
                
            answer = get_ai_response(query)
            
            print(f"Jarvis: {answer}")
            speak(answer)

if __name__ == "__main__":
    run_assistant()