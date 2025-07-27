import pyttsx3
import speech_recognition as sr
import webbrowser 
import os 
import wikipediaapi

def convert_speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something:")
        # Adjust for ambient noise and listen to the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Use Google Web Speech API to recognize the audio
            text = recognizer.recognize_google(audio)
            print(f"You said - {text}")
            return text 
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the request to Google Web Speech API; {e}")


def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def fetch_wikipedia_content(page_title, language='english'):
    # Create a Wikipedia API object
    wiki_wiki = wikipediaapi.Wikipedia(language)

    # Fetch the page content
    page = wiki_wiki.page(page_title)

    # Check if the page exists
    if page.exists():
        # Return the page summary
        return page.summary
    else:
        return f"The page '{page_title}' does not exist on Wikipedia."




while True:
    text = "I am listening"
    text_to_speech(text)
    command = convert_speech_to_text()
    command = command.lower()
    if 'open instagram' in command:
        webbrowser.open("www.instagram.com")
        break 

    if 'control panel' in command:
        os.system("control panel")
        break
    
    if 'python language' in command:
        content=fetch_wikipedia_content('python programming language')
        print(content)
        break

    if 'open youtube' in command:
        webbrowser.open("www.youtube.com")
        break
    

    elif 'exit' in command:
        text_to_speech("Good bye, see you again")
        break

else:
    text_to_speech("I don't know")







    