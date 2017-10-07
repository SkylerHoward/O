import pyttsx3 as pyttsx

class speech():
	def __init__(self):
		self.voice = 0
		self.se = pyttsx.init('sapi5')
		self.se.setProperty('rate', 200)
		self.voices = self.se.getProperty('voices')

	def speak(self, text, print_text=True):
		if print_text:
			print(text)
		self.se.say(text)
		self.se.runAndWait()
		
	def change_voice(self):
		self.voice = (self.voice+1)%2
		self.se.setProperty('voice', self.voices[self.voice].id)
	
	def set_voice(self, i):
		self.voice = i
		self.se.setProperty('voice', self.voices[i].id)