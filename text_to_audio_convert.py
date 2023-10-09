from gtts import gTTS
import playsound
import os
text = "Have a nice day. Good morning everybody"
output = gTTS(text=text,lang='en',slow=False)
output.save('sound.mp3')
playsound.playsound('sound.mp3')
os.remove('sound.mp3')

