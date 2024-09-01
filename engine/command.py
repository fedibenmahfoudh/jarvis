import pyttsx3
import speech_recognition as sr

def speak(text):
  engine = pyttsx3.init()

  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[2].id)   #changing index, changes voices. 1 for female 2 For male

  engine.setProperty('rate', 174)     # setting up new voice rate(voice speed)

  engine.say(text)
  engine.runAndWait()

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source :
    print('listening.....')
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source)

    audio = r.listen(source, 10,6)

  try:
    print('Recognizing')
    query = r.recognize_google(audio_data=audio,language='en-in')
    print(f"user said :{query}")
  except Exception as e:
    return ""
  
  return query.lower()


text = takeCommand()



speak(text);