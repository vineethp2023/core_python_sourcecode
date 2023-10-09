from gtts import gTTS
import os
text = open('demo.txt','r',encoding='utf-8').read()
language='en'
output=gTTS(text=text,lang=language,slow=False)
output.save('filout.mp3')
os.system('start filout.mp3')
