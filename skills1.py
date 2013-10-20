# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_list = []
    for item in some_list:
        if item % 2 != 0:
            odd_list.append(item)
    return odd_list

print all_odd([234, 222, 12, 345, 4, 65, 9, 10,49])

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list = []
    for item in some_list:
        if item % 2 == 0:
            even_list.append(item)
    return even_list

print all_even([234, 222, 12, 345, 4, 65, 9, 10,49])

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_list = []
    for item in word_list:
        if len(item) >= 4:
            long_list.append(item)
    return long_list

print long_words(["kitten", "cat", "turtle", "egg", "balloon", "pie", "turd"])

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    anchor = some_list[0]
    for number in some_list:
        if number < anchor:
            anchor = number # re-assign the anchor variable to number
    return anchor

print smallest([1255, 34, 214, 78, 45, 67])

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    anchor = some_list[0]
    for number in some_list:
        if number > anchor:
            anchor = number
    return anchor

print largest([1255, 34, 214, 78, 45, 67])

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halves_list = []
    for number in some_list:
        halves_list.append(float(number)/2)
    return halves_list

print halvesies([24, 60, 30, 82, 64])

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lenths(word_list):
    lengths_list = []
    for word in word_list:
        lengths_list.append(len(word))
    return lengths_list

print word_lenths(["kitten", "cat", "turtle", "egg", "balloon", "pie", "turd"])

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num # total = total + number
    return total

print sum_numbers([1, 2, 3, 4, 5, 6, 7])

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    total = numbers[0]
    for num in numbers[1:]:
        total *= num
    return total

print mult_numbers([1, 2, 3, 4, 5, 6, 7])

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    new_string = ""
    for stringaling in string_list:
        new_string += stringaling # new_string = new_string + stringaling
    return new_string

print join_strings(["kitten", "cat", "turtle", "egg", "balloon", "pie", "turd"])

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return float(sum_numbers(numbers))/((len(numbers)))

print average([1, 2, 3, 4, 5, 6, 7, 8])
