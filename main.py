import os
import eel
from engine.features import *

eel.init("www")
playAssistantSound()

os.system('start chrome.exe --app="http://localhost:8000/index.html"')
eel.start('index.html',mode=None,host='localhost',block=True) 

""" hetha el code eli majoud fel vidéo """
# os.system('start msedge.exe --app="http://localhost:8000/index.html"')
# eel.start('index.html', mode=None, host='localhost', block=True)
