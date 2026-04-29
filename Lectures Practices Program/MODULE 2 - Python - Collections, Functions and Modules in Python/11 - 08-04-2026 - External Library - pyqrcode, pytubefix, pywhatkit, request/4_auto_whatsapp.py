import pywhatkit
import pyautogui
import time

number = "+919099336762"

pywhatkit.sendwhatmsg_instantly(number, "Start")
time.sleep(5)

message = ["Msg 1", "Msg 2", "Msg 3"]

for msg in message:
    pyautogui.write(msg)
    pyautogui.press("enter")
    time.sleep(5)