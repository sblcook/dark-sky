'''
This class requests, parses, and provides a simple interface for
interacting with the Dark Sky API.
'''
import requests
from Weather import Currently, Daily, Hourly, Minutely
from datetime import datetime
from pprint import pprint


class pyDarkSky:

    def __init__(self, secret_key, latitude, longitude):
        self.url = "https://api.darksky.net/forecast/{}/{},{}".format(secret_key, latitude, longitude)
        self.forecast = requests.get(self.url).json()
        self.currently = self._currently()
        self.daily = self._daily()
        self.hourly = self._hourly()
        self.minutely = self._minutely()
        self.latitude = self.forecast['latitude']
        self.latitude = self.forecast['longitude']
        self.latitude = self.forecast['timezone']

    def _currently(self):
        current_weather = self.forecast['currently']

        apparentTemperature = current_weather['apparentTemperature']
        cloudCover = current_weather['cloudCover']
        dewPoint = current_weather['dewPoint']
        humidity = current_weather['humidity']
        icon = current_weather['icon']
        nearestStormDistance = current_weather['nearestStormDistance']
        ozone = current_weather['ozone']
        precipIntensity = current_weather['precipIntensity']
        precipProbability = current_weather['precipProbability']
        pressure = current_weather['pressure']
        summary = current_weather['summary']
        temperature = current_weather['temperature']
        time = datetime.fromtimestamp(current_weather["time"]).strftime("%-I:%-M%p")
        uvIndex = current_weather['uvIndex']
        visibility = current_weather['visibility']
        windBearing = current_weather['windBearing']
        windGust = current_weather['windGust']
        windSpeed = current_weather['windSpeed']

        return Currently(apparentTemperature, cloudCover, dewPoint, humidity,
                         icon, nearestStormDistance, ozone, precipIntensity,
                         precipProbability, pressure, summary, temperature,
                         time, uvIndex, visibility, windBearing, windGust,
                         windSpeed)

    def _daily(self):
        daily_weather = self.forecast['daily']['data']

        summary = self.forecast['daily']['summary']
        icon = self.forecast['daily']['icon']

        apparentTemperatureHigh = [x.get('apparentTemperatureHigh') for x in daily_weather]
        apparentTemperatureHighTime = [x.get('apparentTemperatureHighTime') for x in daily_weather]
        apparentTemperatureLow = [x.get('apparentTemperatureLow') for x in daily_weather]
        apparentTemperatureLowTime = [x.get('apparentTemperatureLowTime') for x in daily_weather]
        apparentTemperatureMax = [x.get('apparentTemperatureMax') for x in daily_weather]
        apparentTemperatureMaxTime = [x.get('apparentTemperatureMaxTime') for x in daily_weather]
        apparentTemperatureMin = [x.get('apparentTemperatureMin') for x in daily_weather]
        apparentTemperatureMinTime = [x.get('apparentTemperatureMinTime') for x in daily_weather]
        cloudCover = [x.get('cloudCover') for x in daily_weather]
        dewPoint = [x.get('dewPoint') for x in daily_weather]
        humidity = [x.get('humidity') for x in daily_weather]
        icon = [x.get('icon') for x in daily_weather]
        moonPhase = [x.get('moonPhase') for x in daily_weather]
        ozone = [x.get('ozone') for x in daily_weather]
        precipIntensity = [x.get('precipIntensity') for x in daily_weather]
        precipIntensityMax = [x.get('precipIntensityMax') for x in daily_weather]
        precipIntensityMaxTime = [x.get('precipIntensityMaxTime') for x in daily_weather]
        precipProbability = [x.get('precipProbability') for x in daily_weather]
        precipType = [x.get('precipType') for x in daily_weather]
        pressure = [x.get('pressure') for x in daily_weather]
        summary = [x.get('summary') for x in daily_weather]
        sunriseTime = [datetime.fromtimestamp(x.get("sunriseTime")).strftime("%-I:%-M") for x in daily_weather]
        sunsetTime = [datetime.fromtimestamp(x.get("sunsetTime")).strftime("%-I:%-M") for x in daily_weather]
        temperatureHigh = [x.get('temperatureHigh') for x in daily_weather]
        temperatureHighTime = [x.get('temperatureHighTime') for x in daily_weather]
        temperatureLow = [x.get('temperatureLow') for x in daily_weather]
        temperatureLowTime = [x.get('temperatureLowTime') for x in daily_weather]
        temperatureMax = [x.get('temperatureMax') for x in daily_weather]
        temperatureMaxTime = [x.get('temperatureMaxTime') for x in daily_weather]
        temperatureMin = [x.get('temperatureMin') for x in daily_weather]
        temperatureMinTime = [x.get('temperatureMinTime') for x in daily_weather]
        time = [datetime.fromtimestamp(x.get("time")).strftime("%a") for x in daily_weather]
        uvIndex = [x.get('uvIndex') for x in daily_weather]
        uvIndexTime = [x.get('uvIndexTime') for x in daily_weather]
        windBearing = [x.get('windBearing') for x in daily_weather]
        windGust = [x.get('windGust') for x in daily_weather]
        windGustTime = [x.get('windGustTime') for x in daily_weather]
        windSpeed = [x.get('windSpeed') for x in daily_weather]

        return Daily(apparentTemperatureHigh, apparentTemperatureHighTime,
                     apparentTemperatureLow, apparentTemperatureLowTime,
                     apparentTemperatureMax, apparentTemperatureMaxTime,
                     apparentTemperatureMin, apparentTemperatureMinTime,
                     cloudCover, dewPoint, humidity, icon, moonPhase, ozone,
                     precipIntensity, precipIntensityMax,
                     precipIntensityMaxTime, precipProbability, precipType,
                     pressure, summary, sunriseTime, sunsetTime,
                     temperatureHigh, temperatureHighTime, temperatureLow,
                     temperatureLowTime, temperatureMax, temperatureMaxTime,
                     temperatureMin, temperatureMinTime, time, uvIndex,
                     uvIndexTime, windBearing, windGust, windGustTime,
                     windSpeed)

    def _hourly(self):
        hourly_weather = self.forecast['hourly']['data']

        summary = self.forecast['hourly']['summary']
        icon = self.forecast['hourly']['icon']

        apparentTemperature = [x.get('apparentTemperature') for x in hourly_weather]
        cloudCover = [x.get('cloudCover') for x in hourly_weather]
        dewPoint = [x.get('dewPoint') for x in hourly_weather]
        humidity = [x.get('humidity') for x in hourly_weather]
        icon = [x.get('icon') for x in hourly_weather]
        ozone = [x.get('ozone') for x in hourly_weather]
        precipIntensity = [x.get('precipIntensity') for x in hourly_weather]
        precipProbability = [x.get('precipProbability') for x in hourly_weather]
        pressure = [x.get('pressure') for x in hourly_weather]
        summary = [x.get('summary') for x in hourly_weather]
        temperature = [x.get('temperature') for x in hourly_weather]
        time = [datetime.fromtimestamp(x.get("time")).strftime("%-I:%-M%p") for x in hourly_weather]
        uvIndex = [x.get('uvIndex') for x in hourly_weather]
        visibility = [x.get('visibility') for x in hourly_weather]
        windBearing = [x.get('windBearing') for x in hourly_weather]
        windGust = [x.get('windGust') for x in hourly_weather]
        windSpeed = [x.get('windSpeed') for x in hourly_weather]

        return Hourly(apparentTemperature, cloudCover, dewPoint, humidity,
                      icon, ozone, precipIntensity, precipProbability,
                      pressure, summary, temperature, time, uvIndex,
                      visibility, windBearing, windGust, windSpeed)

    def _minutely(self):
        minutely_weather = self.forecast['minutely']['data']

        summary = self.forecast['minutely']['summary']
        icon = self.forecast['minutely']['icon']
        time = [datetime.fromtimestamp(x.get("time")).strftime("%-I:%-M%p") for x in minutely_weather]
        precipIntensity = [x.get('precipIntensity') for x in minutely_weather]
        precipProbability = [x.get('precipProbability') for x in minutely_weather]

        return Minutely(summary, icon, time, precipIntensity,
                        precipProbability)

