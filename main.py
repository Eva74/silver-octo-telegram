from utils import find_avg
from utils import find_median
from utils import rev_list
from utils import is_palindrome
from utils import is_odd_or_even
from utils import int_to_char
from utils import char_to_int

myList = [0, 2, 3, 4, 5, 6]
print("The average of the list is: " + str(find_avg(myList)))
print("The median of the list is " + str(find_median(myList)))
rev_list(myList)
print("The list in reverse is: " + str(myList))

myString = 'salas'
print(is_palindrome(myString))

print("Is the first element in the list even?")
print(is_odd_or_even(myList[0]))

# check if number in list is odd or even
print("The current list is: " + str(myList))
for i in myList:
    if is_odd_or_even(i):
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")

num = 65
print("The number " + str(num) + " is the character:")
print(int_to_char(num))

myChar = 'Z'
print("The character " + myChar + " is the number:")
print(char_to_int(myChar))
