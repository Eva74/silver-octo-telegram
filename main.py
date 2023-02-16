from utils import find_avg
from utils import find_median
from utils import rev_list
from utils import is_palindrome
from utils import is_odd_or_even
from utils import int_to_char
from utils import char_to_int


class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print("The following guests (name, age) have arrived: ")
guest1 = Guest("Maria", 48)
print(guest1.name)
print(guest1.age)

guest2 = Guest("Hidalgo", 36)
print(guest2.name)
print(guest2.age)

guest3 = Guest("Ana", 9)
print(guest3.name)
print(guest3.age)

guestList = [guest1, guest2, guest3]
guestAges = []
for i in guestList:
    guestAges.append(i.age)
print("The guest ages are " + str(guestAges))
print("The average of guest age is: " + str(find_avg(guestAges)))
print("The median of guest age is " + str(find_median(guestAges)))

# check if ages are odd or even. Function returns a Boolean
print("Is the first guests' age even?")
print(is_odd_or_even(guestAges[0]))
for i in guestAges:
    if is_odd_or_even(i):
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")

rev_list(guestAges)
print("The list in reverse is: " + str(guestAges))
for i in guestList:
    if is_palindrome(i.name):
        print(i.name + " is a palindrome")
    else:
        print(i.name)

num = 65
print("The number " + str(num) + " is the character:")
print(int_to_char(num))

myChar = 'Z'
print("The character " + myChar + " is the number:")
print(char_to_int(myChar))

# print out sum of letter is string as ascii numbers
user_string = 'paper'
user_string_ascii = []
for i in user_string:
    user_string_ascii.append(char_to_int(i))
print('The ascii conversion of the given string is: ')
print(user_string_ascii)
user_string_ascii.sort()
print("The sorted list is: ")
print(user_string_ascii)
user_string_ascii_sum = 0
for i in user_string_ascii:
    user_string_ascii_sum += i
print("The sum of the list is: " + str(user_string_ascii_sum))
