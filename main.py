import pyautogui
import keyboard
import time

state = False

# Colors of sticks edges
colors = [(140, 62, 29), (211, 135, 85), (170, 150, 171), (97, 73, 85), (135, 97, 77), (133, 142, 164), (71, 80, 104), (209, 178, 152)]

# If on than bot is working
def switch():
    global state
    state = not state

# Trying to pick an approximate color from our color patterns to confirm the presence of a stick.
def ifColorPattern(color1, color2, colors):
    m1 = 10
    m2 = 10
    for pattern in colors:
        m1 = min(m1, abs(color1[0] - pattern[0]) + abs(color1[1] - pattern[1]) + abs(color1[2] - pattern[2]))
        m2 = min(m2, abs(color2[0] - pattern[0]) + abs(color2[1] - pattern[1]) + abs(color2[2] - pattern[2]))
    
    if min(m1, m2) < 10:
        return True
    else:
        return False

# It makes our P key toggle the bot
keyboard.add_hotkey("p", lambda:switch())

try:
    while True:
        while state:
            time.sleep(0.1) # Doing it slower because screenshots isn't an instant action
            screen = pyautogui.screenshot().load()

            # Taking colors of pixels on the sticks edges
            
            case11 = screen[1100, 705]
            case12 = screen[1060, 705]
            case21 = screen[820, 705]
            case22 = screen[860, 705]

            # Taking color of "next game" button and "ad close" button
            
            case31 = screen[1060, 980]
            case32 = screen[706, 283]
           

            if ifColorPattern(case11, case12, colors): # stick on right
                pyautogui.moveTo(422, 705)
                pyautogui.click()
                pyautogui.click()

            elif ifColorPattern(case21, case22, colors): # stick on left
                pyautogui.moveTo(1296, 705)
                pyautogui.click()
                pyautogui.click()

            elif case31 == (10, 235, 174): # Next game
                pyautogui.moveTo(1060, 980)
                pyautogui.click()

            elif case32 == (255, 255, 255): # Close ad
                pyautogui.moveTo(706, 283)
                pyautogui.click()

            else: # Anyway...
                pyautogui.click()

except KeyboardInterrupt:
    print('\n')


