from pynput.keyboard import Key, KeyCode, Listener
from pynput.mouse import Button, Controller
import ctypes
import webbrowser
import sys
import time

mouse = Controller()

ctypes.windll.user32.MessageBoxW(0, "DO NOT CLOSE THIS ALERTS WITH ENTER!", "ALERT!!!", 0)
ctypes.windll.user32.MessageBoxW(0, "Berat Çimen is the original creator of this program.", "Who made this?", 0)
ctypes.windll.user32.MessageBoxW(0, "First of all don't use Enter to close this window. Left Shift + H = will open this windows again. Also Shift + C opens hotkey window. If you have any problem with the program contact me via: instagram.com/berat.cmn or bit.ly/BeratCimen. ", "Berat Cimen - Fake Hotkeys Usage ", 0)

# Edit this as you want!

def function_1():
    webbrowser.open('https://www.youtube.com/results?search_query=my+mix')
    mouse.position = (610, 247)
    print('Fare şu konuma getirildi: {0}'.format(
        mouse.position))
    time.sleep(1.5)
    mouse.press(Button.left)
    mouse.release(Button.left)

def function_2():
    webbrowser.open('https://www.instagram.com/berat.cmn/')

def function_3():
    print('Executed function_3')
    ctypes.windll.user32.MessageBoxW(0, "Shift + A = Opens my music mix via Youtube. Shift + B opens my IG account. Shift + C = opens this help alert. Shift + Z will close the program.", "HOTKEYS!", 0)

def function_4():
    print('The current pointer position is {0}'.format(
    mouse.position))
    ctypes.windll.user32.MessageBoxW(0, 'The current pointer position is {0}'.format(
    mouse.position) , "Your Mouse Position", 0)

def function_help():
    print('Executed function_help')
    ctypes.windll.user32.MessageBoxW(0, "First of all don't use Enter to close this window. Left Shift + H = will open this windows again. If you have any problem with the program contact me via: instagram.com/berat.cmn or bit.ly/BeratCimen. ", "Berat Cimen - Fake Hotkeys Usage ", 0)

def function_exit():
    print('Executed function_exit')
    ctypes.windll.user32.MessageBoxW(0, "HIT OKAY AND PROGRAM WILL CLOSE.", "EXIT", 0)
    sys.exit()


# Map of the keys , you can add more with your own combinations.
combination_to_function = {
    frozenset([Key.shift, KeyCode(char='a')]): function_1, # No `()` after function_1 because we want to pass the function, not the value of the function
    frozenset([Key.shift, KeyCode(char='A')]): function_1,
    frozenset([Key.shift, KeyCode(char='b')]): function_2,
    frozenset([Key.shift, KeyCode(char='B')]): function_2,
    frozenset([Key.shift, KeyCode(char='c')]): function_3,
    frozenset([Key.shift, KeyCode(char='C')]): function_3,
    frozenset([Key.shift, KeyCode(char='d')]): function_4,
    frozenset([Key.shift, KeyCode(char='D')]): function_4,
    frozenset([Key.shift, KeyCode(char='h')]): function_help,
    frozenset([Key.shift, KeyCode(char='H')]): function_help,
    frozenset([Key.shift, KeyCode(char='z')]): function_exit,
    frozenset([Key.shift, KeyCode(char='Z')]): function_exit,
}

current_keys = set()

def on_press(key):
    current_keys.add(key)

def on_release(key):
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        combination_to_function[frozenset(current_keys)]()
    current_keys.remove(key)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
