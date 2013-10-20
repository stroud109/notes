# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_list = []
    for num in some_list:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

print all_odd([3, 43, 78, 67, 34, 80, 78, 89])


# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list = []
    for num in some_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

print all_even([3, 43, 78, 67, 34, 80, 78, 89])

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_list = []
    for item in word_list:
        if len(item) >= 4:
            long_list.append(item)
    return long_list

print long_words(["mermaid", "chocolate", "pumpkin", "cat", "gal", "star", "pip"])

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    anchor = some_list[0]
    for num in some_list:
        if num < anchor:
            anchor = num
    return anchor

print smallest([3, 43, 78, 67, 34, 80, 78, 89])

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    anchor = some_list[0]
    for num in some_list:
        if num > anchor:
            anchor = num
    return anchor

print largest([3, 43, 78, 67, 34, 80, 78, 89])

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halves_list = []
    for num in some_list:
        halves_list.append(float(num)/2)
    return halves_list

print halvesies([3, 43, 78, 67, 34, 80, 78, 89])

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lenths(word_list):
    lengths_list = []
    for item in word_list:
        lengths_list.append(len(item))
    return lengths_list

print word_lenths(["mermaid", "chocolate", "pumpkin", "cat", "gal", "star", "pip"])

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    anchor = 0
    for num in numbers:
        anchor += num
    return anchor

print sum_numbers([1, 2, 3, 4, 5, 6, 7])

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    anchor = 1
    for num in numbers:
        anchor *= num
    return anchor

print mult_numbers([1, 2, 3, 4])

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    joined_string = ""
    for some_string in string_list:
        joined_string += some_string
    return joined_string

print join_strings(["mermaid", "chocolate", "pumpkin", "cat", "gal", "star", "pip"])

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return float(sum(numbers))/len(numbers)

print average([1, 2, 3, 4, 5, 6, 7, 8])
