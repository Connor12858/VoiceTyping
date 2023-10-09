# Import the libraries needed
from pynput.keyboard import Key, Controller
import time
import win32gui
import mouse


# Creating a new class to utilize the packages and create what we need
# This limits the confusion and simplifies when typing and waiting for voice
class Typing:
    # Upon creating an object, turn the packages into something we can use
    def __init__(self):
        self.keyboard = Controller()
        self.win = win32gui

    # Type a message given
    # Retrieves a string and loops through to enter each character
    def TypeMessage(self, msg):
        for i in msg:
            self.keyboard.type(i)
            time.sleep(0.1)

    # Using cursor information and if mouse is left-clicked we are typing
    # Tell the program that it is time to listen for voice
    def TypeCheck(self):
        if self.GetCursor() == 65541 and mouse.is_pressed("left"):
            return True

    # Find the cursor information and return the value (66539. 66541 are the 2 prominent)
    def GetCursor(self):
        return self.win.GetCursorInfo()[1]
