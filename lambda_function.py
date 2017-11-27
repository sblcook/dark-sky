from pyDarkSky import pyDarkSky
import os

def lambda_handler(event, context):
    print("Received event: " + str(event))
    valid_commands = ['precip', 'now', 'today', 'week']
    
    command = event.get('Body')
    
    if command.lower() not in valid_commands:
        message = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
                  "<Response><Message>\nInvalid Command."\
                  "Commands are 'precip' for the precip probability"\
                  "and 'now' for the current weather\n</Message></Response>"
    else:
        forecast = pyDarkSky(os.environ['dark_sky_key'], os.environ['latitude'], os.environ['longitude']) 
    
        if command.lower() == "precip":
            message = precip(forecast)

        elif command.lower() == 'now':
            message = currentWeather(forecast)  
                      
    return message
    
def currentWeather(forecast):
    current = "\n"
    current += "Current weather in Philadelphia: " + forecast.minutely.summary + "\n"
    current += "Temperature: " + str(int(forecast.currently.temperature)) + "℉\n"
    if forecast.currently.temperature - forecast.currently.apparentTemperature > 1:
         current += "Feels like: " + str(int(forecast.currently.apparentTemperature)) + "℉\n"
    if forecast.currently.uvIndex > 0:
        current += "UV Index: " + str(forecast.currently.uvIndex) + "\n"
    if forecast.currently.windSpeed > 0:
        current += "Wind Speed: " + str(int(forecast.currently.windSpeed)) + " mph\n"
    if forecast.currently.precipProbability > 0:
        current += "Precip Probability: " + str(forecast.currently.precipProbability * 100) + "%\n"
    current += "Humidity: " + str(int(forecast.currently.humidity * 100)) + "%\n"
    current += "Pressure: " + str(int(forecast.currently.pressure)) + " mbar\n"

    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
           "<Response><Message>\n{}</Message></Response>".format(current)  
              
def precip(forecast):
    precip = forecast.minutely.precipProbability[1:]
    n=5
    condensed_precip = [int(sum(precip[i:i+n]) * 10 // n) for i in range(0, len(precip),n)]
    
    fig = ""
    for x in condensed_precip:
        fig += "|{}\n".format('*' * x)
        
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
           "<Response><Message>\nPrecip for next hour (* = 10% chance):\n{}</Message></Response>".format(fig)
