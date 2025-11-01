import speech_recognition as sr
import pyttsx3
import subprocess  
import pyautogui   
import time        
import datetime    
import webbrowser  

# --- 1. Setup Voice and Speech Engines ---


recognizer = sr.Recognizer()

def speak(text):
    """Converts a string of text into audible speech."""
    speech_engine = pyttsx3.init() 
    print(f"Assistant: {text}")
    speech_engine.say(text)
    speech_engine.runAndWait()

def listen_for_command():
    """Listens for a single voice command from the user."""
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Listening timed out, listening again...")
            return None
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        print("Sorry, my speech service is currently down.")
        return None

# --- 3. Main Assistant Loop ---

speak("Hello! I'm online and ready to help.")

while True:
    command = listen_for_command()

    if command is None:
        continue

    # --- 4. Define Your Commands (The fun part!) ---
    
    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "open notepad" in command:
        speak("Sure, opening Notepad for you.")
        subprocess.Popen(['notepad.exe'])
        time.sleep(1)  

    elif "type this" in command:
        speak("Okay, what should I type?")
        text_to_type = listen_for_command()
        if text_to_type:
            speak("Typing in 3 seconds. Click where you want me to type.")
            time.sleep(3)
            pyautogui.typewrite(text_to_type, interval=0.05)
            speak("Done.")

    elif "what time is it" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p") # e.g., "10:04 PM"
        speak(f"The current time is {current_time}")

    # --- THIS WHOLE BLOCK IS NEW ---
    elif "what's the date" in command or "what is the date" in command:
        now = datetime.datetime.now()
        # This formats the date as "Saturday, November 01, 2025"
        current_date = now.strftime("%A, %B %d, %Y")
        speak(f"Today is {current_date}")
   

    elif "open chrome" in command:
        speak("Opening Google Chrome.")
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        try:
            subprocess.Popen([chrome_path])
            time.sleep(1)  
        except FileNotFoundError:
            speak("Sorry, I can't find Google Chrome at that path.")
            speak("Please check the chrome_path variable in the code.")

    elif "close this window" in command or "close this" in command:
        speak("Okay, closing the active window.")
        pyautogui.hotkey('alt', 'f4')

    elif "search for" in command:
        search_query = command.replace("search for", "")
        if search_query:
            speak(f"Searching Google for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            time.sleep(1) 
        else:
            speak("What would you like me to search for?")

    elif "go to sleep" in command:
        speak("Going to sleep. Goodbye.")
        subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"])
        break 

    elif "goodbye" in command or "exit" in command or "stop" in command:
        speak("Goodbye! Shutting down.")
        break  
    
    else:
        if command:

            speak("I'm not sure how to do that yet.")
