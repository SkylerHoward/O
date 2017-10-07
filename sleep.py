import time, morning
from datetime import datetime

def main():
	while True:
		a = time.mktime(datetime.now().timetuple())
		n = datetime.now()
		if n.hour == 6 and (n.minute-(n.minute%5)) == 15:
			return morning.main()
		time.sleep(300 - (time.mktime(datetime.now().timetuple())-a))