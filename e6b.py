
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
