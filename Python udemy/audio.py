
from gtts import gTTS

a=input("Please enter a text:")

# tts = gTTS(text="Hello crazy programmer", lang='en')

tts = gTTS(text=a, lang='en')

tts.save("audio1.mp3")
