import weather, events

def main():
	rtn = []
	rtn.append("Good morning.")
	events_list = events.today()
	rtn.append('You have {} events today'.format(len(events_list)))
	if len(events_list) > 0:
		for i in events_list:
			rtn.append(i)
	forecast_celsius, forecast_kelvin = weather.main()
	rtn.append("The temperature is currently {}C, {}K".format(forecast_celsius['temp'], forecast_kelvin['temp']))
	rtn.append("It is set to reach a high of {}C, {}K".format(forecast_celsius['temp_max'], forecast_kelvin['temp_max']))
	rtn.append("And a low of {}C, {}K".format(forecast_celsius['temp_min'], forecast_kelvin['temp_min']))
	return rtn

if __name__ == '__main__':
	for i in main():
		print(i)
	print('')