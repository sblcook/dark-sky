class Currently:

    def __init__(self, temp, precip_prob, summary, time, wind_spd):
        self.temp = temp
        self.precip_prob = precip_prob
        self.summary = summary
        self.time = time
        self.wind_spd = wind_spd


class Daily:

    def __init__(self, time, min_temp, max_temp, sunrise, sunset,
                 precip_prob, wind_spd):
        self.time = time
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.sunrise = sunrise
        self.sunset = sunset
        self.precip_prob = precip_prob
        self.wind_spd = wind_spd


class Hourly:

    def __init__(self, time, temp, precip_prob, wind_spd):
        self.time = time
        self.temp = temp
        self.precip_prob = precip_prob
        self.wind_spd = wind_spd


class Minutely:

    def __init__(self, time, precip_prob, precip_intensity):
        self.time = time
        self.precip_prob = precip_prob
        self.precip_intensity = precip_intensity

