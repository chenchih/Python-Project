"""
Title:How to make an instagram spam bot
Link: https://www.youtube.com/watch?v=UsNu7VdWHDs
Youtuber/author: Max Codez
status: NOT test Yet
"""
import time, pyautogui
time.sleep(5)
f= open("file.txt", r)
for word in f :
    pyautogui.typewrite(word)