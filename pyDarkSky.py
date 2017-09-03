'''
This class requests, parses, and provides a simple interface for
interacting with the Dark Sky API.
'''
import requests


class pyDarkSky:

    def __init__(self, secret_key, latitude, longitude):
        self.url = "https://api.darksky.net/forecast/{}/{},{}".format(secret_key, latitude, longitude)
        self.weather = requests.get(self.url).json()

    def currently(self):
        return self.weather['currently']

    def daily(self):
        return self.weather['daily']

    def hourly(self):
        return self.weather['hourly']

    def minutely(self):
        return self.weather['minutely']

