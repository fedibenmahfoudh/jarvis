import os
import eel
eel.init("www")
os.system('start chrome.exe --app="http://127.0.0.1:5500/jarvis-main/www/index.html"')
eel.start('index.html',mode=None,host='localhost',block=True)