import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipediaapi


# Initialize recognizer and voice engine
listener = sr.Recognizer()
listener.pause_threshold = 1

machine = pyttsx3.init()


# Text to speech function
def talk(text):
    machine.say(text)
    machine.runAndWait()


# Take voice input
def input_instruction():
    instruction = ""

    try:
        with sr.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)

            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()

            print("You said:", instruction)

    except Exception as e:
        print("Error:", e)

    return instruction


# Main assistant function
def play_Milo():

    instruction = input_instruction()

    if "play" in instruction:
        song = instruction.replace("play", "")
        song = song.replace("milo", "")
        song = song.strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in instruction: 
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " + current_time)

    elif "date" in instruction:
        current_date = datetime.datetime.now().strftime('%m/%d/%Y')
        talk("Today's date is " + current_date)

    elif "how are you" in instruction:
        talk("I am fine. How about you?")

    elif "what is your name" in instruction:
        talk("I am Milo. What can I do for you?")

    elif "who is" in instruction:
        human = instruction.replace("milo", "")
        human = human.replace("who is", "")
        human = human.strip()

    try:

        wiki = wikipediaapi.Wikipedia(
            language='en',
            user_agent='MiloAI/1.0'
        )

        page = wiki.page(human)

        if page.exists():

            info = page.summary[:500]

            print(info)
            talk(info)

        else:
            talk("I could not find information.")

    except Exception as e:
        print("Error:", e)
        talk("Something went wrong.")


# Run assistant
play_Milo()