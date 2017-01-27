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

    def test_fuel_endurance(self):
        '''Test fuel endurance calculation'''
        pass

    def test_average_fuel_consumption(self):
        pass

    def test_fuel_capacity(self):
        pass

class Wind(unittest.TestCase):
    '''Test wind calculations'''

    def test_wind_correction_angle(self):
        '''Test wind correction angle calculation'''
        pass

class Conversionts(unittest.TestCase):
    '''Unit conversions'''

    def test_cel_to_fahr(self):
        pass

    def test_fahr_to_cel(self):
        pass

    def test_nautical_to_statute(self):
        pass

    def test_statute_to_nautical(self):
        pass

if __name__ == '__main__':
    unittest.main()
