from utils import find_avg
from utils import find_median
from utils import rev_list
from utils import is_palindrome

myList = [0, 2, 3, 4, 5, 6]
print("The average of the list is: " + str(find_avg(myList)))
print("The median of the list is " + str(find_median(myList)))
rev_list(myList)
print("The list in reverse is: " + str(myList))

myString = 'salas'
print(is_palindrome(myString))
