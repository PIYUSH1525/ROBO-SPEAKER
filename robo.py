# TEXT TO SPEECH
from gtts import gTTS  # Googler text to speech library
import os
x = input("Enter the text to translate")
language = 'en'
obj = gTTS(text=x, lang=language, slow=False)  # slow is false becuse if this not false then it will play in fast speed
obj.save("file.mp3")
os.system("file.mp3")

# WEATHER APP USING API

