from ctypes.wintypes import HMODULE
from html.parser import HTMLParser
import time
from datetime import datetime
from pyfiglet import Figlet
from art import *
import os

x = 5

while x > 1:
    os.system('cls')
    timenow = datetime.now()
    current_time = timenow.strftime("%H:%M:%S")
    hour = timenow.strftime("%H")
    minutes = timenow.strftime("%M")
    seconds = timenow.strftime("%S")
    displaytext = (f"{hour}:{minutes}:{seconds}")
    displayansi = text2art(displaytext, 'future_1')
    print("------------------------------------------------------------------------")
    print(displayansi)
    print("------------------------------------------------------------------------")
    time.sleep(1)