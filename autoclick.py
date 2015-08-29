import win32api
import win32con #for the VK keycodes
import time
import msvcrt as m
import signal
import sys

def mouseClick(timer):
    if not check_off_pos():
        print("Click!")
        x,y = win32api.GetCursorPos()
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0) 
        time.sleep(timer) 
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0) 
        time.sleep(timer)
        global count
        count = count + 1
        if count >= 3 / (timer * 2):
            cast_spell(timer)
            count = 0

def cast_spell(timer):
    print("Cast Spell!")
    global spell_x
    global spell_y
    global tx
    global ty
    x = spell_x
    y = spell_y
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0) 
    time.sleep(timer) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0) 
    time.sleep(timer)
    win32api.SetCursorPos((tx, ty)) 
    time.sleep(timer)


def getPos():
    x,y = win32api.GetCursorPos()
    return x, y

def wait():
    m.getch()

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

def check_off_pos():
    global tx
    global ty
    a, b = getPos()
    if abs(a - tx) > 100 or abs(b - ty) > 100:
        return 1
    return 0

input("Press Enter to capture of chest...")
tx, ty = getPos()
input("Press Enter to capture of spell...")
spell_x, spell_y = getPos()
count = 0
options = []

signal.signal(signal.SIGINT, signal_handler)
print("Press Ctrl+C")
sleep = 0
while True:
    mouseClick(0.03)
    a, b = getPos()
    if check_off_pos():
        print('sleeping')
        time.sleep(3)
        sleep = sleep + 1
        if sleep == 5:
            input("Press Enter to restart...")
    else:
        sleep = 0
