<<<<<<< HEAD
import os
import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import *
import pywhatkit as kit
=======
from playsound import playsound
import eel
>>>>>>> 0a3d1be499a4b28efc66d030454ef74b5d769deb

# playing assistant sound function 
@eel.expose
def playAssistantSound():
<<<<<<< HEAD
    music_dir = "www/assets/audio/start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")    
    query=query.replace("open","")  
    query.lower()  

    if query!="":
        speak("opening"+query)
        os.system("start"+query)
    else:
        speak("not found")

def playYoutube(query):
    query=query.replace(ASSISTANT_NAME,"")    
    query.lower()  

    if query!="":
        search_term=extract_yt_term(query)
        speak("playing"+search_term+"on Youtube")
        kit.playonyt(search_term)
    else:
        speak("not found")
   

def extract_yt_term(command):
    #extract a regular expression pattern to capture the song name
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    #use re.search to find the match in the command 
    match=re.search(pattern,command,re.IGNORECASE)
    #if a match was found return the exact same name of the song ,otherwise return none 
    return match.group(1) if match else None



=======
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

>>>>>>> 0a3d1be499a4b28efc66d030454ef74b5d769deb
