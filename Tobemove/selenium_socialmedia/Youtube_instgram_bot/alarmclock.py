"""
Title:Custom Alarm clock 
Link: https://www.youtube.com/watch?v=fwMdqqu_yOQ
Youtuber/author: Max Codez
status: TEST PASS
"""


import time
from playsound import playsound
from datetime import datetime
alarmtime= "14:04"
while True:
    localtime= datetime.now().strftime('%H:%M')
    if localtime == alarmtime:
        playsound("Kalimba.mp3")
        break
    else:
        print("not yet")
        time.sleep(10)
