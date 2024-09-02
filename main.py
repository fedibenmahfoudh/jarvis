import os
import eel
from engine.features import *
<<<<<<< HEAD
from engine.command import *

eel.init('www')
playAssistantSound()




eel.start('index.html')  # Or whichever file is your main HTML file

# os.system('start chrome.exe --app="http://127.0.0.1:5500/www/index.html"')
# eel.start('index.html',mode=None,host='localhost',block=True) 
=======

eel.init("www")
playAssistantSound()

os.system('start chrome.exe --app="http://localhost:8000/index.html"')
eel.start('index.html',mode=None,host='localhost',block=True) 
>>>>>>> 0a3d1be499a4b28efc66d030454ef74b5d769deb

""" hetha el code eli majoud fel vidéo """
# os.system('start msedge.exe --app="http://localhost:8000/index.html"')
# eel.start('index.html', mode=None, host='localhost', block=True)
