import unittest
from utils import find_median
from utils import find_avg
from utils import is_palindrome


class MyTestCase(unittest.TestCase):

    def test_median(self):
        #  test odd set
        mylist = [1, 2, 3]
        self.assertEqual(find_median(mylist), 2)
        #  test even set
        mylist2 = [1, 2, 3, 4]
        self.assertEqual(find_median(mylist2), ('2', '3'))

    def test_average(self):
        #  test average in list
        mylist = [0, 1, 2, 3]
        self.assertEqual(find_avg(mylist), 1.5)

    def test_is_palindrome(self):
        #  test if the string is a palindrome
        mystring = 'potatoes'
        self.assertEqual(is_palindrome(mystring), False)
        mystring2 = 'salas'
        self.assertEqual(is_palindrome(mystring2), True)

