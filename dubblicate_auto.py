import time
from random import randint

import nxbt
from nxbt import Buttons
from nxbt import Sticks

nx = nxbt.Nxbt()
controller_idx = nx.create_controller(
    nxbt.PRO_CONTROLLER,
    reconnect_address=nx.get_switch_addresses())


def init():

    nx.wait_for_connection(controller_idx)
    nx.press_buttons(controller_idx,[Buttons.A],)
    time.sleep(2)
    nx.press_buttons(controller_idx,[Buttons.A])
    time.sleep(2)



def open_secound_menu():
    nx.press_buttons(controller_idx, [Buttons.A])
    time.sleep(1)
    nx.press_buttons(controller_idx,[Buttons.DPAD_DOWN])
    time.sleep(1)
    nx.press_buttons(controller_idx,[Buttons.X])
    time.sleep(1)
    nx.press_buttons(controller_idx, [Buttons.A])
    time.sleep(2)
    nx.press_buttons(controller_idx, [Buttons.R])
    time.sleep(2.5)
    nx.press_buttons(controller_idx, [Buttons.X])

def getItem(Button_Direction):
    for index in range(0,6):
        nx.press_buttons(controller_idx, [Buttons.A])
        time.sleep(0.6)
        nx.press_buttons(controller_idx,[Buttons.DPAD_DOWN])
        time.sleep(0.6)
        nx.press_buttons(controller_idx, [Buttons.A])
        time.sleep(0.6)
        nx.press_buttons(controller_idx, [Buttons.A])
        time.sleep(0.6)
        nx.press_buttons(controller_idx, [Buttons.A])
        time.sleep(0.6)
        nx.press_buttons(controller_idx,[Button_Direction])

def getSloth():
    for slot in range(0, 5):
        if (slot % 2) == 0:
            getItem(nxbt.Buttons.DPAD_RIGHT)
            nx.press_buttons(controller_idx, [Buttons.DPAD_LEFT])
            time.sleep(0.6)
        if (slot % 2) != 0:
            getItem(nxbt.Buttons.DPAD_LEFT)
            nx.press_buttons(controller_idx, [Buttons.DPAD_RIGHT])
            time.sleep(0.6)

        nx.press_buttons(controller_idx,[Buttons.DPAD_DOWN])
        time.sleep(0.8)

def back_To_First_Menu():
    nx.press_buttons(controller_idx,[Buttons.B])
    time.sleep(1.0)
    nx.press_buttons(controller_idx, [Buttons.B])
    time.sleep(1.0)
    nx.press_buttons(controller_idx, [Buttons.B])
    time.sleep(1.0)
    nx.press_buttons(controller_idx, [Buttons.A])
    time.sleep(1.0)
    nx.press_buttons(controller_idx, [Buttons.B])
    time.sleep(1.0)



def start_Macro():
   for i in range(0, 10):
        open_secound_menu()
        getSloth()
        back_To_First_Menu()
        time.sleep(1.0)






# Start the NXBT service


init()
start_Macro()


