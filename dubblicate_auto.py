webpage="Google Chrome" #Name of the web browswer you are using.

waittime=18.4

from pynput.keyboard import Key, Controller
import time
import win32com.client as comclt

#Define function to press a key twice. This is the primarily used function to avoid missing a button press
def Key_Press_Twice(key):
    keyboard.press(key)

    time.sleep(.1)
    keyboard.release(key)

    time.sleep(.1)

    keyboard.press(key)

    time.sleep(.1)
    keyboard.release(key)

#Define function to press a key once.
def Key_Press_Once(key):
    print(key)
    keyboard.press(key)
    time.sleep(.1)
    keyboard.release(key)





wsh= comclt.Dispatch("WScript.Shell") # Allow the script to automatically change to the correct tab



keyboard = Controller() # Initialize the keyboard to use as a Controller

print("Starting in 3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("live")


wsh.AppActivate(webpage)#Switch to the correct tab


def index_in_list():
    v = 0;
    for v in range(0, 6):

        Key_Press_Once('l')
        time.sleep(0.6)
        Key_Press_Once('s')
        time.sleep(0.2)
        Key_Press_Once('l')
        time.sleep(0.6)
        Key_Press_Once('l')
        time.sleep(0.8)
        Key_Press_Once('l')
        time.sleep(0.5)
        Key_Press_Once('d')
        time.sleep(0.3)



def rows():
    l = 0;
    for l in range(0, 5):
        index_in_list()
        if l != 5:
            Key_Press_Once('d')
            time.sleep(0.2)
            Key_Press_Once('s')





for i in range(0, 10):
    print(i)

    time.sleep(1.5)
    Key_Press_Once('l')
    time.sleep(2)
    Key_Press_Once('s')
    time.sleep(2)
    Key_Press_Once('i')
    time.sleep(2.5)
    Key_Press_Once('l')
    time.sleep(2)
    Key_Press_Twice('9')
    time.sleep(2.5)
    Key_Press_Once('i')
    time.sleep(1)

    rows()
    time.sleep(2)
    Key_Press_Once('k')
    time.sleep(2)
    Key_Press_Once('k')
    time.sleep(2)
    Key_Press_Once('k')
    time.sleep(2)
    Key_Press_Once('l')
    time.sleep(2)
    Key_Press_Once('k')
    time.sleep(2.3)
