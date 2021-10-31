#from _typeshed import NoneType
import pyttsx3                  #pip install pyttsx3 
import datetime        
import speech_recognition as sr #pip install speechRecognizer 
import wikipedia                #pip install wikipedia
import smtplib
import webbrowser as wb    
import psutil                  #pip install psutil 
import pyjokes                 #pip install pyjokes
import os 
import pyautogui               #pip install pyautogui  
import random 
import json
import requests
from urllib.request import urlopen 
import wolframalpha             #pip install wolframalpha  
import time 
from datetime import date

"""
pip install wheel
pip install pipwin
pipwin install PyAudio

"""


engine = pyttsx3.init()
wolframalpha_app_id = '6VPTV6-9TWWUV3T5E'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time=datetime.datetime.now().strftime('%I:%M:%S')
    speak('current time is')
    speak(Time)


def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("Current date is")
    #speak([date,month,year])
    speak(date)
    speak(month)
    speak(year)


def wishme():

    speak("Welcome back")
    #time_()
    #date_()

    #greetings
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<15:
        speak("Good Afternoon")
    elif hour>=15 and hour<24:
        speak("Good Evening")
    else:
        speak("Good Night")
    
    speak("please tell me How can i help you")


def TakeCommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("listining........")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing.......")
        query=r.recognize_google(audio,language="en-US")
        print(query)

    except Exception as e:
        print(e)
        print("Say Again please")
        return None

    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail,com',587)
    server.ehlo()
    server.starttls
    #your email must me less secure to use as a sender
    
    server.login('v1i1j1a1y1p@gmail.com','Vijay@123')
    server.sendmail('v1i1j1a1y1p@gmail.com',to,content)
    server.close()


def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery=psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def screenshot():
    img=pyautogui.screenshot()
    date1=datetime.datetime.now().strftime('%H%M%S')
    imgname=date1
    path='G:/Projects/Screenshot/screenshot data/'+date1+'.png'
    img.save(path)

if __name__=="__main__":

    wishme()

    while True:
        query=TakeCommand().lower()
        '''if query:
            query=query.lower()
        else:
            continue'''

        #All comands will be stored in lower case

        if "time" in query:#tell us local time
            time_()

        elif "date" in query:#tell us date
            date_()

        elif "wikipedia" in query:
            speak("searching")
            query=query.replace("wikipedia",'')
            result=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "send email" in query:
            try:
                speak("What should I send")
                content=TakeCommand()
                speak("Who is the receiver")
                receiver=input("Enter the Receiver Email ")
                to=receiver
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Unable to sent Email")

        elif "search in chrome" in query:
            speak('what should i search')
            chromepath='C:/Users/VIJAY.P/AppData/Local/Google/Chrome/Application/chrome.exe %s'

            search=TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search in youtube' in query:
            speak("Wnat should i search?")
            search_Term=TakeCommand().lower()
            speak('Here we go to youtube')
            wb.open("https://www.yourube,com/results?search_query="+search_Term)

        elif 'search in google' in query:
            speak('what should I search?')
            search_Term=TakeCommand().lower()
            speak('Searching')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'go offline' in query:
            
            speak('Have a nice day')
            speak('Going offline')
            quit()

        elif 'word' in query:
            speak('opening Ms Word')
            ms_word='path of ms word'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak('what should I write')
            notes=TakeCommand()
            file=open('notes.txt','w')
            speak('Should I include date and time')
            ans=TakeCommand().lower()

            if 'yes' in ans or 'sure' in ans:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking notes')
            
            else:
                file.write(notes)
                speak('Done writing notes')
            
        elif 'show note' in query:
            speak('showing notes')
            file.open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            speak('Taking screenshot')
            screenshot()
            speak('Saving sceenshot')

        elif 'play music' in query:
            songs_dir='D:/asus/Download/Music'
            music=os.listdir(songs_dir)
            speak('what should I play?')
            speak('Select a number')
            ans=TakeCommand().lower()
            while ('number' not in ans and 'random' not in ans and 'your choice' not in ans and 'you choose' not in ans and 'choose yourself' not in ans):
                speak('I could not understand you . Please try again')
                ans=TakeCommand().lower()
            if 'number' in ans:
                no=int(ans.replace('number',''))
            elif 'random' or 'your choice' or 'you choose' or 'choose yourself' in ans:
                no=random.randint(1,20)
                #else:
                #no=random.randint(1,20)
            os.startfile(os.path.join(songs_dir,music[no]))
        
        elif 'remember that' in query:
            speak('What should I  remember')
            memory=TakeCommand()
            speak('You asked me to remember that '+memory)
            remember=open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember=open('memory.txt','r')
            speak('You asked me remember that'+remember)

        elif 'news' in query:
            try:
                jsonObj=urlopen('https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=d9cb6df23012457ca4651c3e0d4aa056')
                data=json.load(jsonObj)
                i=1
                speak('Here is some of the news')
                print("-----=====TOP ARTICLES=====-----")

                for item in data['articles']:
                    print(str(i)+'.'+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1
            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query=query.replace('where is ','')
            location=query
            speak('YOU asked to locate'+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'calculate' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            indx=query.lower().split().index('calculate')
            query=query.split()[indx+1:]
            res=client.query(''.join(query))
            answer=next(res.results).text
            print('The answer is :'+answer)
            speak('The answer is '+answer)

        elif 'what is' or 'who is' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            res=client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print('No results')

        elif 'stop listening' in query:
            speak('For how many seconds you want me to stop litening to your commands?')
            ans=int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'hi' or 'hai' in query:
            speak('Hello')

        elif 'logout' in query:
            os.system('shutdown -l')
        elif 'restart' in query:
            os.system('shutdown /r /t/ 1')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

            


        




    



