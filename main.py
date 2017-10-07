import weather, morning, time, sleep, events
from datetime import datetime

from speak import *

speak = speech()

def main():
	while True:
		command = input('> ')
		if command == 'sleep':
			speak.speak('Good night.')
			for line in sleep.main():
				speak.speak(line)
		if command == 'quit':
			quit()
		if command == 'events':
			te = events.today()
			speak.speak('You have {} events today'.format(len(te)))
			for line in te:
				speak.speak(line)


main()