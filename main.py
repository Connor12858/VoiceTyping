# Import our own modules
from typingModule import Typing
from voiceModule import Voice

# Use our packages
kb = Typing()
v = Voice()


# Our run method that will run
def Run():
    while True:
        if kb.TypeCheck():
            msg = v.Listen()
            kb.TypeMessage(msg)

# Entry point into the program
if __name__ == "__main__":
    Run()
