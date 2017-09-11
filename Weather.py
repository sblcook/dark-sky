class Currently:

    def __init__(self, apparentTemperature, cloudCover, dewPoint, humidity,
                 icon, nearestStormDistance, ozone, precipIntensity,
                 precipProbability, pressure, summary, temperature, time,
                 uvIndex, visibility, windBearing, windGust, windSpeed):

        self.apparentTemperature = apparentTemperature
        self.cloudCover = cloudCover
        self.dewPoint = dewPoint
        self.humidity = humidity
        self.icon = icon
        self.nearestStormDistance = nearestStormDistance
        self.ozone = ozone
        self.precipIntensity = precipIntensity
        self.precipProbability = precipProbability
        self.pressure = pressure
        self.summary = summary
        self.temperature = temperature
        self.time = time
        self.uvIndex = uvIndex
        self.visibility = visibility
        self.windBearing = windBearing
        self.windGust = windGust
        self.windSpeed = windSpeed


class Daily:

    def __init__(self, apparentTemperatureHigh, apparentTemperatureHighTime,
                 apparentTemperatureLow, apparentTemperatureLowTime,
                 apparentTemperatureMax, apparentTemperatureMaxTime,
                 apparentTemperatureMin, apparentTemperatureMinTime,
                 cloudCover, dewPoint, humidity, icon, moonPhase, ozone,
                 precipIntensity, precipIntensityMax, precipIntensityMaxTime,
                 precipProbability, precipType, pressure, summary, sunriseTime,
                 sunsetTime, temperatureHigh, temperatureHighTime,
                 temperatureLow, temperatureLowTime, temperatureMax,
                 temperatureMaxTime, temperatureMin, temperatureMinTime, time,
                 uvIndex, uvIndexTime, windBearing, windGust, windGustTime,
                 windSpeed):

        self.apparentTemperatureHigh = apparentTemperatureHigh
        self.apparentTemperatureHighTime = apparentTemperatureHighTime
        self.apparentTemperatureLow = apparentTemperatureLow
        self.apparentTemperatureLowTime = apparentTemperatureLowTime
        self.apparentTemperatureMax = apparentTemperatureMax
        self.apparentTemperatureMaxTime = apparentTemperatureMaxTime
        self.apparentTemperatureMin = apparentTemperatureMin
        self.apparentTemperatureMinTime = apparentTemperatureMinTime
        self.cloudCover = cloudCover
        self.dewPoint = dewPoint
        self.humidity = humidity
        self.icon = icon
        self.moonPhase = moonPhase
        self.ozone = ozone
        self.precipIntensity = precipIntensity
        self.precipIntensityMax = precipIntensityMax
        self.precipIntensityMaxTime = precipIntensityMaxTime
        self.precipProbability = precipProbability
        self.precipType = precipType
        self.pressure = pressure
        self.summary = summary
        self.sunriseTime = sunriseTime
        self.sunsetTime = sunsetTime
        self.temperatureHigh = temperatureHigh
        self.temperatureHighTime = temperatureHighTime
        self.temperatureLow = temperatureLow
        self.temperatureLowTime = temperatureLowTime
        self.temperatureMax = temperatureMax
        self.temperatureMaxTime = temperatureMaxTime
        self.temperatureMin = temperatureMin
        self.temperatureMinTime = temperatureMinTime
        self.time = time
        self.uvIndex = uvIndex
        self.uvIndexTime = uvIndexTime
        self.windBearing = windBearing
        self.windGust = windGust
        self.windGustTime = windGustTime
        self.windSpeed = windSpeed


class Hourly:

    def __init__(self, apparentTemperature, cloudCover, dewPoint, humidity,
                 icon, ozone, precipIntensity, precipProbability, pressure,
                 summary, temperature, time, uvIndex, visibility, windBearing,
                 windGust, windSpeed):

        self.apparentTemperature = apparentTemperature
        self.cloudCover = cloudCover
        self.dewPoint = dewPoint
        self.humidity = humidity
        self.icon = icon
        self.ozone = ozone
        self.precipIntensity = precipIntensity
        self.precipProbability = precipProbability
        self.pressure = pressure
        self.summary = summary
        self.temperature = temperature
        self.time = time
        self.uvIndex = uvIndex
        self.visibility = visibility
        self.windBearing = windBearing
        self.windGust = windGust
        self.windSpeed = windSpeed


class Minutely:

    def __init__(self, summary, icon, time, precipIntensity,
                 precipProbability):

        self.summary = summary
        self.icon = icon
        self.time = time
        self.precipIntensity = precipIntensity
        self.precipProbability = precipProbability
