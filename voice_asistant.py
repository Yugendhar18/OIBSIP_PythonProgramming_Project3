import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess 

engine = pyttsx3.init()

music_process = None

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech service is unavailable.")
            return ""

def respond(command):
    global music_process  
    if "hello" in command:
        speak("Hello there! How can I help you?")
    elif "time" in command:
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time_str}")
    elif "date" in command:
        date_str = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date_str}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching Google for {query}")
        webbrowser.open(url)
    elif "chatgpt" in command:
        speak("Opening ChatGPT.")
        url = "https://chat.openai.com"
        webbrowser.open(url)
    elif "youtube" in command:
        speak("Opening YouTube.")
        url = "https://www.youtube.com"
        webbrowser.open(url)
    else:
        speak("Sorry, I didn't understand that.")

# Run the assistant
speak("Voice Assistant is now active. Please say something.")

while True:
    user_command = get_audio()
    if user_command:
        if "exit" in user_command :
            speak("Goodbye!")
            break
        respond(user_command)