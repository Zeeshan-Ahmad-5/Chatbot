import speech_recognition as sr
import webbrowser
import pyttsx3
import urllib.parse
import json
import requests  # Added for news fetching
from openai import OpenAI
from dotenv import dotenv_values

secrets = dotenv_values(".env")
openAiKey = secrets["OPENAI_KEY"]
newsKey = secrets["NEWS_KEY"]

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(api_key = openAiKey)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content


def get_news():
    # Replace 'your_api_key' with your actual News API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={newsKey}"
    
    try:
        response = requests.get(url)
        news_data = response.json()
        
        if news_data["status"] == "ok":
            articles = news_data["articles"][:10]  # Fetch top 10 news articles
            news_list = [f"Headline: {article['title']}" for article in articles]
            return news_list
        else:
            return ["Could not fetch the news at this moment."]
    except Exception as e:
        return [f"Error fetching news: {e}"]
    

def ProcessCommand(command):
    print(f"Processing command: {command}")  # Debugging log
    if "google" in command.lower():
        try:
            webbrowser.open("https://www.google.com")
        except Exception as e:
            print(f"Error opening Google: {e}")
    elif "youtube" in command.lower():
        try:
            webbrowser.open("https://www.youtube.com")
        except Exception as e:
            print(f"Error opening YouTube: {e}")
    # elif "play" in command.lower():  # New feature
    #     search_term = command.lower().replace("play", "").strip()
    #     if search_term:
    #         speak(f"Playing {search_term} on YouTube")
    #         query = urllib.parse.quote(search_term)
    #         url = f"https://www.youtube.com/results?search_query={query}"
    #         webbrowser.open(url)
    #     else:
            speak("I didn't catch what you want to play.")
    elif "linkedin" in command.lower():
        try:
            webbrowser.open("https://www.linkedin.com")
        except Exception as e:
            print(f"Error opening LinkedIn: {e}")
    elif "facebook" in command.lower():
        try:
            webbrowser.open("https://www.facebook.com")
        except Exception as e:
            print(f"Error opening Facebook: {e}")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = music_library.Music[song]
        webbrowser.open(link)
    elif "news" in command.lower():  # New news feature
        speak("Fetching the latest news...")
        news = get_news()
        for item in news:
            print(item)
            speak(item)
    else:
        # Let OpenAI handle the request
        output = aiprocess(command)
        speak(output)
        

if __name__ == "__main__":
    speak("Initializing Friday....")
    while True:
        print("Listening for wake word 'Friday'...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            print("Recognizing...")
            word = recognizer.recognize_google(audio)
            print(f"Wake word detected: {word}")
            if word.lower() == "friday":
                speak("Yes boss")
                with sr.Microphone() as source:
                    print("Friday is active...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print(f"Command received: {command}")
                ProcessCommand(command)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
