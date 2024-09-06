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
    
    else:
      print("dont run ")
        

  except :
    print("error")

  eel.ShowHood()







