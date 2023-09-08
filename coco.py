import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')  
#print(voices[0].id) 
engine.setProperty('voice',voices[1].id)
# speak function = We can make the computer speak with Python.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# wishme hame wish krta ha time k hisab se or speak funstion k through .    
def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour>>0 and hour<<12 :
        speak("good morning")
    elif hour>=12 and hour<18 :
        speak("good afternoon")
    else :
        speak("good evening")
speak("i am Coco sir . how may i help you")    
'''takeCommand() function, our A.I. assistant will return a
  string output by taking microphone input from the user.'''             
def takecommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
       print("listening.....")
       ''' pause_threhold = the number of seconds the system will 
        take to recognize the voice after the user has completed their sentence.
        user द्वारा अपना वाक्य पूरा करने के बाद आवाज को पहचानने में लगने वाले सेकंड की संख्या है। '''
       r.pause_threshold = 1
       audio = r.listen(source)
   try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
   except Exception as e :
         print(e)
   
         print("say again")
         return"none" 
   return query 
''' try = ye tab likte ha jab hame lage ki error aa sakta ha ''' 
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yashrajkharniwal@gmail.com','cmkvalwgrqvlpwgg')
    server.sendmail('yashrajkharniwal@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
   wishME()
   while True:
   #if 1:
    query = takecommand().lower()
#logic for executing task based on query
    if 'wikipedia' in query:
        speak('searching wikipidea.....')
        query=query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=3)
        speak("according to wikipdia")
        print(results)
        speak(results)
    
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open whatsapp' in query:
        webbrowser.open("web.whatsapp.com")
    elif 'play music' in query:
        music_dir='D:\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"bro,the time is{strTime}")    
    elif'open vs code' in query:
        codepath = "C:\\Users\\yashr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
        os.startfile(codepath)
    elif'send email' in query:
        try:
            speak("what should i say?")
            content = takecommand()
            to = "Vishvjeetsinghrathore751@gmail.com"
            sendEmail(to,content)
            speak("email has been send")
        except Exception as e:
            print(e)
            speak("the email is not sended bro")
            
    elif 'open notepad' in query:
        openpage="C:\\Users\\yashr\\OneDrive\\Documents"
        os.startfile(openpage)
    elif'open chrome' in query:
        cromepath="C:\\Users\\yashr\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(cromepath)

          