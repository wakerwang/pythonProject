# coding:utf-8
import unittest
from city_functions import city_full_name


class CityTestClass(unittest.TestCase):
    def test_city_country(self):
        """可向形参 population 传递值吗？"""
        santiago_chile = city_full_name('santiago', 'chile', population=5_000_000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - Population 5000000')


if __name__ == '__main__':
    unittest.main()
