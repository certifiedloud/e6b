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

class Wind(unittest.TestCase):
    '''Test wind calculations'''

    def test_wind_correction_angle(self):
        '''Test wind correction angle calculation'''
        pass

if __name__ == '__main__':
    unittest.main()
