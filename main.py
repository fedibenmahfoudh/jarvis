import os
import eel
from engine.features import *
from engine.command import *

eel.init('www')
playAssistantSound()




eel.start('index.html')  # Or whichever file is your main HTML file

# os.system('start chrome.exe --app="http://127.0.0.1:5500/www/index.html"')
# eel.start('index.html',mode=None,host='localhost',block=True) 

""" hetha el code eli majoud fel vidéo """
# os.system('start msedge.exe --app="http://localhost:8000/index.html"')
# eel.start('index.html', mode=None, host='localhost', block=True)
