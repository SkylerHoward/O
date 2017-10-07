import pyowm, json, os, time
from datetime import datetime


def main():
	if os.path.isfile('weather.json'): 
		with open("weather.json", "r") as file:
			weather = json.loads(file.read())
	ctt = datetime.now().timetuple()
	elapsed = time.mktime(ctt) - weather['time']
	if elapsed < 600:
		return weather['weather']
	API_key = "API_KEY"
	owm = pyowm.OWM(API_key)
	observation = owm.weather_at_place('LOCATION')
	w = observation.get_weather()
	temp_list = [w.get_temperature('celsius'), w.get_temperature()]
	weather['weather'] = temp_list
	weather['time'] = time.mktime(datetime.now().timetuple())
	with open("weather.json", "w") as file: 
		file.write(json.dumps(weather))
	return temp_list
