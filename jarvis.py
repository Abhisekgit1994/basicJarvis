import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        engine.say('Good Morning sir!')
    else:
        engine.say('Welcome back Sir.')
    engine.say('How can I help you today?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You:{query}\n")

    except Exception as e:
        print(e)
        print('Sorry I could not recognise , please say that again ...')
        # speak('Sorry I could not recognise , please say that again ...')
        return "None"
    return query


if __name__ == '__main__':

    while True:
        query = takeCommand().lower()
        # if "None" in query:
        #     continue

        if 'kara' in query:
            wishMe()
            query = takeCommand().lower()

            if 'please tell some details about ' in query:
                speak('searching wikipedia')
                query = query.replace('please tell some details about', '')
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak("According to wikipedia")
                speak(results)

            if 'open' in query:
                speak("opening")
                if 'youtube' in query:
                    speak("youtube")
                    webbrowser.open('https:\\www.youtube.com')
                if 'hotstar' in query:
                    speak("hotstar")
                    webbrowser.open('https://www.hotstar.com/in')
            if 'play' in query:
                if 'video' in query:
                    video_dir = 'D:\\The Flash'
                    videos = os.listdir(video_dir)
                    print(videos)
                    os.startfile(os.path.join(video_dir,videos[2]))
        

