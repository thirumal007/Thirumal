import pyttsx3
import datetime
from pyttsx3 import engine
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Thiru')
        
    elif hour>=12 and hour<18:
        speak('Good Afternoon Thiru')
        
    else:
        speak('Good  Night Thiru')
    speak('how can i help     u ')
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening  .................')
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print('Wait for few minutes')
        query=r.recognize_google(audio,language="en-in")
        print('user said',query)
        
    except Exception as e :
        speak('say that again pleasse ')
        query='nothing'
    
    return query

if __name__ == '__main__':
    speak('welcome boss nan jarvis')
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching in wikipedia')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            speak(results)
            print(results)
        
        elif ' open Youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverfl')
            
        elif 'music play' in query:
            musdir ='F:\songs'
            songs=os.listdir(musdir)
            print(songs)
            os.startfile(os.path.join(musdir,songs[2])) 
            
        elif 'the time ' in query:
            time=datetime.datetime.now().strftime("%H %M")
            speak(time)
                                   
            
            
            
        elif "take rest" in query:
            speak("I  am  quitting")
            quit()