import speech_recognition as sr
import pyttsx3
#import pywhatkit
import datetime
import wikipedia
import pyjokes

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def takecommand():
    try:
        with sr.Microphone() as source:
            print ('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print (command)
    except:
        pass
    return command


def runAlexa():
    command = takecommand()
    print (command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        #pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        search = command.replace('who is', '')
        person = wikipedia.summary(search, 1)
        print(person)
        talk(person)
    elif 'what is' in command:
        search = command.replace('what is', '')
        objectName = wikipedia.summary(search, 1)
        print(objectName)
        talk(objectName)
    elif 'date' in command:
        talk('Sure... I will be quite happy to do that..')
    elif 'are you single' in command:
        talk('Yes... I am  ...')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I did not get that. Please say it again')


while True:
    runAlexa()
