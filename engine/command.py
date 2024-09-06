import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
  engine = pyttsx3.init()

  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female 2 For male

  engine.setProperty('rate', 174)     # setting up new voice rate(voice speed)
  eel.DisplayMessage(text)
  engine.say(text)
  engine.runAndWait()

@eel.expose
def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source :
    print('listening.....')
    eel.DisplayMessage('listening.....')
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source)

    audio = r.listen(source, 10,6)

  try:
    print('Recognizing')
    eel.DisplayMessage('Recognizing.....')
    query = r.recognize_google(audio_data=audio,language='en-GB')
    print(f"user said :{query}")
    eel.DisplayMessage(query)
    time.sleep(2)
   
  except Exception as e:
    return ""
  
  return query.lower()

@eel.expose
def allCommands():
  try:

    query=takeCommand()
    print(query)

    if "open" in query:
      from engine.features import openCommand
      openCommand(query)
      
    elif " play on youtube":
      from engine.features import playYoutube
      playYoutube(query)
    elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            message = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    message = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    message = 'call'
                else:
                    message = 'video call'
                    
                whatsApp(contact_no, query, message, name)
    else:
      print("dont run ")
        

  except :
    print("error")

  eel.ShowHood()







