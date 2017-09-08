'''
This class requests, parses, and provides a simple interface for
interacting with the Dark Sky API.
'''
import requests
from Weather import Currently, Daily, Hourly, Minutely
from datetime import datetime


class pyDarkSky:

    def __init__(self, secret_key, latitude, longitude):
        self.url = "https://api.darksky.net/forecast/{}/{},{}".format(secret_key, latitude, longitude)
        self.weather = requests.get(self.url).json()
        self.currently = self._currently()
        self.daily = self._daily()
        self.hourly = self._hourly()
        self.minutely = self._minutely()

    def _currently(self):
        current_weather = self.weather['currently']

        temp = current_weather['temperature']
        precip_prob = current_weather['precipProbability']
        summary = current_weather['summary']
        time = datetime.fromtimestamp(current_weather['time']).strftime("%-I:%-M%p")
        wind_spd = current_weather['windSpeed']

        return Currently(temp, precip_prob, summary, time, wind_spd)

    def _daily(self):
        daily_weather = self.weather['daily']['data']

        days = [datetime.fromtimestamp(x.get("time")).strftime("%a") for x in daily_weather]
        min_temps = [x.get("apparentTemperatureMin") for x in daily_weather]
        max_temps = [x.get("apparentTemperatureMax") for x in daily_weather]
        sunrise_times = [datetime.fromtimestamp(x.get("sunriseTime")).strftime("%-I:%-M") for x in daily_weather]
        sunset_times = [datetime.fromtimestamp(x.get("sunsetTime")).strftime("%-I:%-M") for x in daily_weather]
        precip_probs = [x.get("precipProbability") for x in daily_weather]
        wind_speeds = [x.get("windSpeed") for x in daily_weather]

        return Daily(days, min_temps, max_temps, sunrise_times, sunset_times,
                     precip_probs, wind_speeds)

    def _hourly(self):
        hourly_weather = self.weather['hourly']['data']

        times = [datetime.fromtimestamp(x.get("time")).strftime("%-I:%-M%p") for x in hourly_weather]
        temps = [x.get("apparentTemperature") for x in hourly_weather]
        precip_probs = [x.get("precipProbability") for x in hourly_weather]
        wind_speeds = [x.get("windSpeed") for x in hourly_weather]

        return Hourly(times, temps, precip_probs, wind_speeds)

    def _minutely(self):
        minutely_weather = self.weather['minutely']['data']

        times = [datetime.fromtimestamp(x.get("time")).strftime("%-I:%-M%p") for x in minutely_weather]
        precip_probs = [x.get("precipProbability") for x in minutely_weather]
        precip_intensities = [x.get("precipIntensity") for x in minutely_weather]

        return Minutely(times, precip_probs, precip_intensities)
