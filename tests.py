from e6b import E6B
import unittest

class TimeSpeedDistance(unittest.TestCase):
    '''Test time, speed and distance calculations'''

    def setUp(self):
        self.e6b = E6B()

    def test_time(self):
        '''Test time calculations'''
        time = self.e6b.time(1, 60)
        self.assertEqual(60, time)

    def test_speed(self):
        '''Test speed calculations'''
        speed = self.e6b.speed(1, 60)
        self.assertEqual(60, speed)

    def test_distance(self):
        '''Test distance calculations'''
        distance = self.e6b.time(1, 60)
        self.assertEqual(60, distance)

class Fuel(unittest.TestCase):
    '''Fuel calculations'''
    def setUp(self):
        self.e6b = E6B()

    def test_fuel_endurance(self):
        '''Test fuel endurance calculation'''
        pass

    def test_average_fuel_consumption(self):
        pass

    def test_fuel_capacity(self):
        pass

class Wind(unittest.TestCase):
    '''Test wind calculations'''
    def setUp(self):
        self.e6b = E6B()

    def test_wind_correction_angle(self):
        '''Test wind correction angle calculation'''
        pass

class Conversions(unittest.TestCase):
    '''Unit conversions'''
    def setUp(self):
        self.e6b = E6B()

    def test_cel_to_fahr(self):
        fahr = self.e6b.cel_to_fahr(0)
        self.assertEqual(32, fahr)

    def test_fahr_to_cel(self):
        cel = self.e6b.fahr_to_cel(32)
        self.assertEqual(0, cel)

    def test_nautical_to_statute(self):
        stat = self.e6b.nautical_to_statute(10)
        self.assertEqual(11.51, stat)

    def test_statute_to_nautical(self):
        naut = self.e6b.statute_to_nautical(20)
        self.assertEqual(17.38, naut)

if __name__ == '__main__':
    unittest.main()
