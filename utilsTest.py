import unittest
from utils import find_median
from utils import find_avg
from utils import is_palindrome
from utils import is_odd_or_even
from utils import int_to_char
from utils import char_to_int


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
        s = 'potatoes'
        self.assertEqual(is_palindrome(s), False)
        s = 'salas'
        self.assertEqual(is_palindrome(s), True)

    def test_is_odd_or_even(self):
        #  test if the input(int) is even
        num = 2
        num2 = 1
        self.assertEqual(is_odd_or_even(num), True)
        self.assertEqual(is_odd_or_even(num2), False)

    def test_int_to_char(self):
        # test if the characters are returned after inputting numbers
        mylist = [72, 101, 108, 108, 111]
        output = ''
        for i in mylist:
            output += str(int_to_char(i))
        self.assertEqual(output, 'Hello')

    def test_chr_to_int(self):
        # test if the proper integers return after inputting a character
        mychar = 'o'
        self.assertEqual(char_to_int(mychar), 111)

