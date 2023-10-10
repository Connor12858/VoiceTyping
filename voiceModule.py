# Import the libraries needed
import speech_recognition as sr

import secrets


# Define a voice module that will hear the user
# Listen to the user until a pause and send it back as a string
class Voice:
    # Upon creating an object, turn the packages into something we can use
    def __init__(self):
        self.mic = sr.Microphone()
        self.rec = sr.Recognizer()

    # Listen until there is silence
    def Listen(self):
        # Use the microphone for audio source
        with self.mic as source:
            print("Hi")
            # read the audio data from the default microphone
            audio_data = self.rec.listen(source)
            # convert speech to text
            try:
                text = self.rec.recognize_google(audio_data, key=secrets.speech_key)
            except:
                return ""
            # return the data
            print("Bye")
            return text

