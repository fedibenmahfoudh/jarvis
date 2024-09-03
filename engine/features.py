import sqlite3
import os
import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import *
import pywhatkit as kit
import webbrowser

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# playing assistant sound function 
@eel.expose
def playAssistantSound():

    music_dir = "www/assets/audio/start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")    
    query=query.replace("open","")  
    query.lower()  

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                  'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")


def playYoutube(query):
    query=query.replace(ASSISTANT_NAME,"")    
    query.lower()  

    if query!="":
        search_term=extract_yt_term(query)
        speak("playing "+search_term+" on Youtube")
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




