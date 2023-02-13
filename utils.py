import math


def find_avg(list_of_nums):
    return sum(list_of_nums) / len(list_of_nums)


def find_median(list_of_nums):
    if len(list_of_nums) % 2 == 1:
        x = math.floor(len(list_of_nums)/2)
        return list_of_nums[x]
    else:
        x = math.floor(len(list_of_nums)/2)
        y = x-1

        return str(list_of_nums[y]), str(list_of_nums[x])


def rev_list(list_of_nums):
    return list_of_nums.reverse()


def is_palindrome(string):
    arr = []
    arr2 = []

    for i in string:
        arr.append(i)
    for i in arr:
        arr2.insert(0, i)
    print("Is the string a palindrome? ")
    if arr == arr2:
        return True
    else:
        return False


def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def int_to_char(num):
    return chr(num)


def char_to_int(character):
    return ord(character)

