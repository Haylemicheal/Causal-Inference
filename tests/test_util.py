import unittest
import sys, os
import io
import pandas as pd
sys.path.append(os.path.abspath(os.path.join('..')))

from scripts.utils import Util

class TestUtil(unittest.TestCase):
    def test_date_split(self):
        """Test the date_split method"""
        util = Util()
        date = "2021-07-01 09:30:59"
        year, month, day, hour = util.split_date(date)
        self.assertEqual(year, '2021')
        self.assertEqual(month, '07')
        self.assertEqual(day,'01')
    
    def test_time_split(self):
        """Test the time_split method"""
        util = Util()
        time = "09:30:59"
        hour, minute, sec = util.split_time(time)
        self.assertEqual(hour, '09')
        self.assertEqual(minute, '30')

    def test_distance(self):
        """Test get distance method"""
        start = ["6.6010417","3.2766339"]
        end = ["6.4501069","3.3916154"]
        util = Util()
        distance = util.get_distance(start, end)
        distance = "{:.6f}".format(distance)
        self.assertEqual(distance, '20.984319')

if __name__ == '__main__':
    unittest.main()