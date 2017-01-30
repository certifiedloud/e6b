import math

class E6B(object):
    def __init__(self):
        pass

    def time(self, speed, distance):
        return distance / speed

    def speed(self, time, distance):
        return distance / time

    def distance(self, time, speed):
        return speed * time

    def cel_to_fahr(self, degrees_cel):
        return (degrees_cel * 9/5) + 32

    def fahr_to_cel(self, degrees_fahr):
        return (degrees_fahr - 32) * 5/9

    def nautical_to_statute(self, nautical):
        return round(nautical * 1.1507794, 2)

    def statute_to_nautical(self, statute):
        return round(statute / 1.1507794, 2)

    def wind_correction_angle(self, course, true_airspeed, wind_dir, wind_speed):
        wca = (180/math.pi) * math.asin((wind_speed / true_airspeed) *
            math.sin(math.pi * (wind_dir - course) / 180))
        # round to the nearest whole degree
        return round(wca, 0)

    def density_altitude(self, pressure_alt, oat_cel, ISA):
        # return 145442.16 * (1 - (17.326 * pressure_alt / 459.67 + oat_cel) ** 0.235)
        return pressure_alt + 118.8 * (oat_cel - ISA)
