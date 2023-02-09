from utils import find_avg
from utils import find_median
from utils import rev_list
from utils import is_palindrome
from utils import is_odd_or_even
from utils import int_to_char

myList = [0, 2, 3, 4, 5, 6]
print("The average of the list is: " + str(find_avg(myList)))
print("The median of the list is " + str(find_median(myList)))
rev_list(myList)
print("The list in reverse is: " + str(myList))

myString = 'salas'
print(is_palindrome(myString))

print("Is the first element in the list even?")
print(is_odd_or_even(myList[0]))

num = 65
print(int_to_char(num))
