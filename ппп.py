from gtts import gTTS
from playsound import playsound
import os
language = 'ru'
s = gTTS("")
s.save('sample.mp3')
playsound('sample.mp3')