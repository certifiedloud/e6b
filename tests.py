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

    def test_true_airspeed(self):
        pass

    def test_climb_rate(self):
        pass

class Altitude(unittest.TestCase):
    '''Altitude calculations'''

    def test_pressure_altitude(self):
        pass

    def test_density_altitude(self):
        pass

    def test_true_altitude(self):
        pass

    def test_indicated_altitude(self):
        pass

    def test_required_climb_rate(self):
        pass

    def test_required_descent_rate(self):
        pass

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

class Conversions(unittest.TestCase):
    '''Unit conversions'''

    def test_cel_to_fahr(self):
        pass

    def test_fahr_to_cel(self):
        pass

    def test_nautical_to_statute(self):
        pass

    def test_statute_to_nautical(self):
        pass

    def test_fuel_gallons_to_pounds(self):
        pass

    def test_fuel_pounds_to_gallons(self):
        pass

if __name__ == '__main__':
    unittest.main()
