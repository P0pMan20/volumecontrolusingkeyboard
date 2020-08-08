import keyboard
isVolCtrl = False
activeKey = 'u'
volUpKey = "o"
volDownKey = "p"
import time
def changeState():
    global isVolCtrl
    if keyboard.is_pressed(activeKey) == True and isVolCtrl == False:
        isVolCtrl = True
        keyboard.press_and_release("volume_up")
        keyboard.press_and_release("volume_down")
        print("VolumeCtrlOn")
        time.sleep(1)

    elif keyboard.is_pressed(activeKey) == True and isVolCtrl == True:
        print("VolumeCtrlOff")

        isVolCtrl = False
        time.sleep(1)


while True:
    changeState()
    if isVolCtrl == True:
        if keyboard.is_pressed(volUpKey) == True:
            print("up")
            keyboard.press_and_release("volume_up")
            time.sleep(0.1)
        elif keyboard.is_pressed(volDownKey) == True:
            print("down")
            keyboard.press_and_release("volume_down")
            time.sleep(0.1)