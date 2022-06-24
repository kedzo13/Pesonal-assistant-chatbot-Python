import pyttsx3 # pip install pyttsx3  biblioteka za umetanje govora
import datetime
import os 
import speech_recognition as sr
import wikipedia
import smtplib  #biblioteka za slanje emaila
import webbrowser as wb

engine=pyttsx3.init() 

#kreiramo funkciju za govor
def speak (audio): 
    engine.say(audio) 
    engine.runAndWait()

#funkcija za vrijeme (sat,minuta,sekunda)
def time():
    time=datetime.datetime.now().strftime("%I:%M:%S") #funkcija za doznat vrijeme, prvo govori sate pa minute pa sekunde
    speak("the current time is ")
    speak(time)

def date():
    speak("the current date is")
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)

    speak(date)
    speak(month)
    speak(year)


def greeting():
    speak("Welcome back sir!!!")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning sir")
    elif hour >= 12 and hour<18:
        speak("Good afternoon sir")
    elif hour >=18 and hour<24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("Jarvis at your service. Please tell me how can I help you.")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source: #definiramo mikrofon ka izvor 
        print("Listening...")
        r.pause_threshold=1 #kad pokrenemo ceka 1 sekundu 
        audio=r.listen(source) 

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language ='en-cro')
        print(query)

    except Exception as e:
        print(e)
        speak("Please, say that again")
        return "None"
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('testmoj192@gmail.com', 'Test-1234' )
    server.sendmail('testmoj192@gmail.com', to, content)
    server.close()


if __name__=="__main__":
    greeting()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            try:
                speak("Searching")
                query= query.replace("wikipedia","")
                result=wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except Exception as e:
                print(e)
                speak("I was unable to find any data on that topic, please repeat")
        
        elif 'send email' in query:
            try:
                speak("What should I send?")
                content=takeCommand()
                to = 'mestrovic.josipa@gmail.com'
                sendemail(to, content)
                speak("Sir email has been sent!")
            except Exception as e:
                print(e)
                speak ("I am sorry Sir, I was unable to send the email.")

        elif "google" in query:
            speak("What should I search")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search= takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com' )
        
        elif 'take a note' in query:
            speak("What should I remember?")
            data= takeCommand()
            notes=open('notes.txt','w')
            notes.write(data)
            notes.close()
            speak("I remembered the note sir")

        elif 'read my notes' in query:
            notes=open("notes.txt", "r")
            speak("Sir youre note is: " +notes.read())
            notes.close()


        elif 'offline' in query:
            speak("I am going offline, enjoy youre day sir")
            quit()
            

