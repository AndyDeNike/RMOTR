#Unit2/Intro to Collections/Class1

'''
1) Create Empty List

It's time to dive into one of most common types of collections, lists!

They are great for storing groups of data, especially if order is 
important.

A list is denoted by square brackets and looks like this:

a_list = ["i", "am", "a", "list!"]

Let's start out basic. Extremely basic.

In this assignment, all you need to do is create an empty list! Get em.
'''

my_list = []

# Test Cases

def test_empty_list():
    assert my_list == [], "Seems like my_list is not an empty list"
    assert type(my_list) == list
    assert len(my_list) == 0



'''
2) Create List with One Element

Great news! You have been given a special opportunity to make another list! Yes!

This time, create one with just one element or item in it. You also need to count how many elements the list my_list has with the len function: it's obviously 1 ;)

For this assignment, we will make that item be a predefined variable about chickens.

Good luck.

'''

# First, we need to set up a variable.
# Replace the ? with how many chickens you think have crossed the road 
#today.
number_of_chickens = 1242351

# Set up a new list `my_list` containing the number_of_chickens variable! 
#Wooo!
my_list = [number_of_chickens]

length_of_my_list = len(my_list)  # Use the `len` function to count how 
#many items `my_list` has.
        
# Test Cases

def test_list_one_elem():
    assert my_list == [number_of_chickens], "Your list doesn't contain the number of chickens :("
    assert length_of_my_list == 1



'''
3) Create List with Three Elements

What? You want more practice with lists?! Geez, you must really like 
them. Fine.

This time, we're going to expand on the previous assignment.

What's better than a list with one element? A list with three elements. 
Great!

Use the three word variables word1, word2 and word3 to create a list 
pizza_time that contains those three words.
'''

# Enter 3 words to describe pizza
word1 = 'delicioso'
word2 = 'maltomario'
word3 = 'bazivamindaro'

# Now make a list containing each of these words and store in a variable called `pizza_time`.
pizza_time = [word1, word2, word3]

# Test Cases

def test_list_three_elem():
    assert type(pizza_time) == list
    assert len(pizza_time) == 3
    assert pizza_time == [word1, word2, word3]
    assert type(word1) == str
    assert type(word2) == str
    assert type(word3) == str



'''
4) Create List with Literals

You don't always have to put variables in your lists. You can also just directly
put data in there.

Example:

fancy_list = ["i am data that is not stored in a variable! OMG!"]

Want to know something cool? Lists are very progressive!
They are heterogeneous and support diversity! That means that you can put
multiple data types inside the same list. Integers, booleans, strings, floats, other lists, everything is good here! Safe space.

For this assignment, create a list named heterogeneous and put an integer, a string, and a boolean in it. In that order.
'''

# Create a list named `heterogeneous` and put a integer, string, and boolean in it.
heterogeneous = [12, 'string', True]
       
# Test Cases        
             
def test_list_literals():
    assert type(heterogeneous) == list, "Oops, heterogeneous is not a list"

    assert len(heterogeneous) == 3

    assert type(heterogeneous[0]) == int
    assert type(heterogeneous[1]) == str
    assert type(heterogeneous[2]) == bool



'''
5) Append to list

The append_to_list functions receives two parameters, hungry_list and data. Its job is to append the data passed to the hungry_list. Examples:

a_list = ['pizza', 'bacon']
modified_list = append_to_list(a_list, 'hamburger')

print(modified_list)  # ['pizza', 'bacon', 'hamburger']
'''

def append_to_list(hungry_list, data):
    hungry_list.append(data)
    return hungry_list

# Test Cases

def test_append_empty_list():
    assert append_to_list([], "list food") == ["list food"]

def test_append_bigger_list():
    assert append_to_list(["pizza", "nachos"], "chips") == ["pizza", "nachos", "chips"]



'''
6) First - Second - Third - Last

The function insert_human receives a list, a position and an element to insert (similar to the insert method). The difference is that the position is specified in a "human" manner. Examples:

list_1 = ['a', 'b', 'c']

insert_human(list_1, 'first', 'Z')
print(list_1)  # ['Z', 'a', 'b', 'c']

list_2 = ['a', 'b', 'c']

insert_human(list_2, 'second', 'Z')
print(list_2)  # ['a', 'Z','b', 'c']

list_3 = ['a', 'b', 'c']

insert_human(list_3, 'last', 'Z')
print(list_3)  # ['a','b', 'c', 'Z']
'''

def insert_human(a_list, position, elem):
    if position == 'first':
        index = 0 
    elif position == 'second':
        index = 1 
    elif position == 'third':
        index = 2 
    elif position == 'last':
        index = len(a_list)
    
    a_list.insert(index, elem)

# Test Cases
               
def test_second_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'second', 'X')
    assert list_1 == ['a', 'X', 'b', 'c']

def test_last_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'last', 'X')
    assert list_1 == ['a', 'b', 'c', 'X']

def test_third_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'third', 'X')
    assert list_1 == ['a', 'b', 'X', 'c']

def test_first_position():
    list_1 = ['a', 'b', 'c']

    insert_human(list_1, 'first', 'X')
    assert list_1 == ['X', 'a', 'b', 'c']


'''
7) Check for Something in List

When Christmas rolls around, everybody knows Santiago, AKA Santa,
has to check his list twice.

Lets help him do that!

Create a function that uses the keyword in to verify if there are any
good students in his list. Check for the string good_student and return 
True or False depending if it is present.
'''

def check_for_good_student(good_bad_student_list):
    if 'good_student' in good_bad_student_list:
        return True
    return False
               
# Test Cases

def test_not_present_in_list():
    assert check_for_good_student(['bad_student', 'terrible_student', 'Santiago']) == False
 
def test_present_in_list():
    assert check_for_good_student(['bad_student', 'good_student', 'decent_student']) == True


'''
8) Is even and contains red

Write a function is_even_and_contains_red that receives a list (containing 
colors) and returns True if the list contains the color "red" AND has 
an even number of elements. False, otherwise. Check the examples:

# 4 elements (even) with red:
is_even_and_contains_red(['red', 'blue', 'green', 'white'])  # True

# 3 elements (odd!) with red:
is_even_and_contains_red(['red', 'blue', 'green'])  # False

# 2 elements (even!) **WITHOUT** red:
is_even_and_contains_red(['white', 'blue', 'green', 'black'])  # False

# 3 elements (odd!) **WITHOUT** red:
is_even_and_contains_red(['white', 'blue', 'green'])  # False
'''

def is_even_and_contains_red(a_list):
    if "red" in a_list and len(a_list) % 2 == 0:
        return True 
    return False

# Test Cases

def test_even_with_red():
    assert is_even_and_contains_red(['red', 'blue', 'green', 'white']) == True

def test_even_without_red():
    assert is_even_and_contains_red(['black', 'blue', 'green', 'white']) == False

def test_odd_with_red():
    assert is_even_and_contains_red(['red', 'blue', 'green']) == False

def test_odd_without_red():
    assert is_even_and_contains_red(['blue', 'green', 'white']) == False



'''
9) Remove from List

Let's fix this list and make it better by removing the word "not" from it. Use the remove method.
'''

not_a_lie = ["i", "am", "not", "perfect"]

not_a_lie.remove('not')
print(not_a_lie)

# Test Cases

def test_remove():
    assert not_a_lie == ["i", "am", "perfect"]



'''
10) Pop from List

Pop element 2 from this_list_is_poppin and store the result in the variable i_am_really.
'''

this_list_is_poppin = ["have", "a", "great", "day"]

# Replace the ? below with your code to pop!
i_am_really = this_list_is_poppin.pop(2)
print(i_am_really)
print(this_list_is_poppin)

# Test Cases

def test_pop():
    assert this_list_is_poppin == ["have", "a", "day"]
    assert i_am_really == "great"



'''
11) Get Bookmark Index

Complete the function get_bookmark_index so that it searches the parameter list_of_pages
and returns the index of the word "bookmark".
'''

def get_bookmark_index(list_of_pages):
    return list_of_pages.index("bookmark")

# Test Cases

def test_get_bookmark_index():
    assert get_bookmark_index([27, 35, 100, "bookmark", 111]) == 3



'''
12) Get Third Element

Complete the get_third_elem function so it always returns the third element in the list.
Because the first two elements looked at us funny.
'''

def get_third_elem(list_of_stuff):
    return list_of_stuff[2]

# Test Cases

def test_get_third_elem():
    assert get_third_elem(["not this one", "not this either", "this one!!!"]) == "this one!!!"



'''
13) Get Second to Last Element

Using indexes to count forwards in lists is cool, but going in reverse has style.

Complete the get_second_to_last_elem function so it always returns the second to last element from the end of the list.
'''

def get_second_to_last_elem(list_of_stuff):
    return list_of_stuff[-2]

# Test Cases

def test_second_to_last_elem():
    assert get_second_to_last_elem([1, 2, 3, 4, 5, 6, 7, 8, 'MEMEMEMEMEEEE', 9]) == 'MEMEMEMEMEEEE'



'''
1) Create a one element tuple

The function one_element_tuple currently returns the value None. Modify it to return a tuple containing just 1 element, the one passed as a parameter:

one_element_tuple('a')  # ('a', )
one_element_tuple(9)    # (9, )
'''

def one_element_tuple(arg):
    return (arg,)

# Test Cases

def test_with_integer():
    assert one_element_tuple(7) == (7, )

def test_with_string():
    assert one_element_tuple('rmotr') == ('rmotr', )



'''
2) Transform list to tuple

Write a function list_2_tuple that takes a list as a parameter and returns a tuple containing the same elements. Example:

list_2_tuple([1, 'c', 9, False])  # (1, 'c', 9, False)
list_2_tuple([2])                 # (2,)
'''

def list_2_tuple(a_list):
    return tuple(a_list)

# Test Cases

def test_with_many_elements():
    assert list_2_tuple(['a', 3, True, 9]) == ('a', 3, True, 9)

def test_with_one_element():
    assert list_2_tuple([7]) == (7, )



'''
1) Sum of numbers in list

Define a function sum_of_numbers_in_list that receives a list of numbers
a_list of an unknown length and calculates the sum of those numbers using a
for loop. Do not use the sum function.

Examples:

>>> sum_of_numbers_in_list([])
0
>>> sum_of_numbers_in_list([4])
4
>>> sum_of_numbers_in_list([2, 3])
5
>>> sum_of_numbers_in_list([2, 3, 4])
9
'''

def sum_of_numbers_in_list(a_list):
    sum = 0
    for i in a_list:
        sum += i
    return sum 

# Test Cases 

def test_empty_list():
    assert sum_of_numbers_in_list([]) == 0

test list of 1 - Run Test

def test_list_of_1():
    assert sum_of_numbers_in_list([4]) == 4

test list of 3 - Run Test

def test_list_of_3():
    assert sum_of_numbers_in_list([2, 3, 4]) == 9

test list of 2 - Run Test

def test_list_of_2():
    assert sum_of_numbers_in_list([2, 3]) == 5



'''
2) Sum if list only contains integers

Define a function sum_if_list_of_ints that receives a list and uses a loop
to make sure the list only contains integers. If so, it returns the sum of
the integers. If not, return 'not an int'.

Hint: Use isinstance again to determine the type.
'''

def sum_if_list_of_ints(a_list):
    for i in a_list:
        if isinstance(i, int) != True:
            return 'not an int'
    return sum(a_list) 

# Test Cases

def test_empty_list():
    assert sum_if_list_of_ints([]) == 0

test sum of ints - Run Test

def test_sum_of_ints():
    assert sum_if_list_of_ints([1, 2, 3]) == 6

test mixed list - Run Test

def test_mixed_list():
    assert sum_if_list_of_ints([1, 'a', 3]) == 'not an int'



'''
3) Reverse a list

Write a function that takes in a list and returns the list reversed.

reverse_a_list([1, 2, 3, 4]) == [4, 3, 2, 1]
'''
def reverse_a_list(list):
    return list[::-1]

# Test Cases 

def test_reverse_a_list_with_strings():
    assert reverse_a_list([
        'eggs', 'flour', 'sugar', 'chocolate']) == [
            'chocolate', 'sugar', 'flour', 'eggs']

def test_reverse_a_list_with_ints():
    assert reverse_a_list([1, 2, 3, 4]) == [4, 3, 2, 1]

'''
4) Get Average

Complete the function get_average so that it returns the average of all the numbers
in list_of_numbers.

You'll need to use a for loop to calculate the total value of all the numbers added together.

Then divide the total by the amount of items in your list to get your average.

Hint: You'll need a variable to keep track of the total. You need to figure out whether that variable
belongs inside or outside the for loop.
'''

# Test Cases 

def test_get_average():
    assert get_average([5, 10, 6]) == 7



'''
5) Create counting list

Define a function create_counting_list that receives a number to count up
to. Normally because you know the number of loops you would want to use a for
loop but in this case we will use a while loop to emulate a for loop.

Return a list where each element counts up to the number provided starting from 1. If
the number provided to count to is negative, return 'cannot be negative'.
'''

def create_counting_list(count_to_number):
    list = []
    if count_to_number == 0:
        return list 
    elif count_to_number < 0:
        return 'cannot be negative'
    for i in range(1, count_to_number+1):
        list.append(i) 
    return list
    
'''
#alt solution 
def create_counting_list(count_to_number):
    counting_list = []
    count = 0
    if count_to_number >= 0:
        while count < count_to_number:
            count += 1
            counting_list.append(count)
        return counting_list
return 'cannot be negative'
'''

# Test Cases

def test_count_to_3():
    assert create_counting_list(3) == [1, 2, 3]

def test_do_not_count():
    assert create_counting_list(0) == []

def test_count_to_7():
    assert create_counting_list(7) == [1, 2, 3, 4, 5, 6, 7]

def test_negative():
    assert create_counting_list(-1) == 'cannot be negative'


'''
6) Powers of 2

You've done something similar to this with a while loop, now do it with a for loop! You'll have to use the range() function.

Complete powers_of_2 using a for loop so that receives the power and returns 2 to that power.

Examples:

>>> powers_of_2(0)
1

>>> powers_of_2(1)
2

>>> powers_of_2(2)
4

>>> powers_of_2(3)
8
'''

def powers_of_2(power):
    total = 1 
    for i in range(power):
        total *= 2 
    return total 
    
# Test Cases 

def test_powers_of_2():
    assert powers_of_2(3) == 8
    assert powers_of_2(1) == 2
    assert powers_of_2(0) == 1


'''
7) 
String Positions

Sometimes you need to know the position of a character in a string and you might not want to count to figure it out. So write a quick function to do it for you!

Complete get_string_positions so that it takes the_string and creates a new string showing the position of each character. Example:

print(get_string_positions("xyz"))

Prints:
0-x
1-y
2-z

The function uses the enumerate() function on the list in a for loop to get each position and character associated with it. Example:

for position, character in enumerate(list_name):
    # do stuff

Then just store the result in a big string. Note you separate the lines by using '\n' the newline character after each line. Good luck!

Hint: You might have to put str() around to position to change it from an integer into a string so you can add it to your result string.
'''

def get_string_positions(the_string):
    result = ""
    for index, char in enumerate(the_string):
        result += "{}-{}\n".format(index, char)
    return result

# Test Cases

test_string_positions():
    assert get_string_positions("abcd") == "0-a\n1-b\n2-c\n3-d\n"



'''
8) Get Positions of Char

Use a for loop with enumerate to complete the function get_positions_of_char so that it looks at another_string and searches for characters that match char_being_searched_for. If it's a match, add the position to a result string followed by a comma. Example:

get_positions_of_char("aabcda", "a") # Returns "0,1,5,"

Hint: You might have to put str() around to position to change it from an integer into a string so you can add it to your result string.
'''

def get_positions_of_char(another_string, char_being_searched_for):
    result = ""
    for idx, letter in enumerate(another_string):
        if letter == char_being_searched_for:
            result += (str(idx)+',')
    return result 

'''
#alt solution 
def get_positions_of_char(another_string, char_being_searched_for):
    result = ""
    for idx, letter in enumerate(another_string):
        if letter == char_being_searched_for:
            result += "{},".format(idx)
    return result 
'''

# Test Cases

def test_get_positions():
    assert get_positions_of_char("XabcXdefXjahX", "X") == "0,4,8,12,"



'''
9) Count Elements with 's'

Complete the function count_elems_with_s so that it uses a for loop to go through each
item in list_of_treasure.

If the letter 's' is in the item, keep count of it.

Return the final count of items that contain the letter 's'.
'''

def count_elems_with_s(list_of_treasure):
    count = 0
    for i in list_of_treasure:
        if 's' in i:
            count += 1 
    return count 

# Test Cases 

def test_count_elems_with_s():
    assert count_elems_with_s(["gold", "silver", "bronze", "steel", "soup"]) == 3



'''
10) Subtract Reversed

Using a while loop, write a function subtract_reversed that receives a list and subtracts all the numbers, starting from the end. Example:

subtract_reversed([3, 7, 18]) # Result: 8 (18 - 7 - 3)
subtract_reversed([9]) # Result: 9 (9 - 0....)

Special case: If the list is empty, should return 0. Check the tests for details.
'''

def subtract_reversed(a_list):
    if a_list == []:
        return 0 
    rev_list = a_list[::-1]
    total = rev_list[0]
    for i in rev_list[1:]:
        total -= i 
    return total 

# Test Cases

def test_list_with_many_elements():
    assert subtract_reversed([2, 7, 9, 32]) == (32 - 9 - 7 - 2)

def test_empty_list():
    assert subtract_reversed([]) == 0

def test_with_one_element():
    assert subtract_reversed([11]) == 11

def test_list_with_two_elements():
    assert subtract_reversed([11, 82]) == (82 - 11)



'''
11) Get Search Match Indexes

It's time to search our list_being_frisked for "suspicious" items. We want you to
return the a new list containing the indexes of any items that match the string "suspicious".

Hint: You'll need to keep track of the index and create a new list to store the indexes in.

Good luck! You wanted to work for the TSA, right?
'''

def get_search_match_indexes(list_being_frisked, search_term):
    detect_list = []
    for idx, item in enumerate(list_being_frisked):
        if item == search_term:
            detect_list.append(idx)
    return detect_list
            
# Test Cases

def test_get_search_match_indexes():
    assert get_search_match_indexes(["glasses", "suspicious", "pen", "suspicious"], "suspicious") == [1, 3]



'''
12) List Challenge

Think you're a master of lists already? Let's see what you got.

Follow the comments to do all kinds of list operations to hopefully get a secret message at the end!
'''

# Are you ready for this? Follow along with the steps to get the secret message

var1 = "lists"
var2 = "made"

# Create a list in the variable list_one with the data "summer", 1, 0, 1, 0, 1, and "fall" in that order
list_one = ["summer", 1, 0, 1, 0, 1, "fall"]

# Create a list in the variable list_two with the data "cake", "with", "in", False, and "nooo" in that order
list_two = ["cake", "with", "in", False, "nooo"]

# Create a list in the variable list_three with the data "all", "RMOTR", "programs", "love", and "me" in that order
list_three = ["all", "RMOTR", "programs", "love", "me"]

# Create an empty list and store it in the variable secret_message
secret_message = []

# Append the second item of list_three to secret_message
secret_message.append(list_three[1])

# Pop the third item from list_two and store it in a variable called var3
var3 = list_two.pop(2)

# Write an if statement checking if the length of list_two is 4
# If it is, append var2 to secret_message
# Otherwise, append the first item of list_two to secret_message
if len(list_two) == 4:
    secret_message.append(var2)
else: 
    secret_message.append(list_two[0])

# Create a list in the variable list_four with the last element from list_three in it
list_four = [list_three[-1]]


# Write an if statement checking if length of list_one is 8
# If it is, remove "love" from list_three
# Otherwise, append the last element of list_one to list_four
if len(list_one) == 8:
    list_three.remove("love")
else: 
    list_four.append(list_one[-1])
# Use list addition to add secret_message and list_four together, storing the result in secret_message. Can use += here
secret_message += list_four

# Append var3 to secret_message
secret_message.append(var3)

# Write an if statement checking if "cake" is in secret_message
# If it is, pop the 5th item and then the 4th item from secret_message
# Otherwise, append the 4th item of list_three to secret_message
if "cake" in secret_message:
    secret_message.pop(4)
    secret_message.pop(3)
else: 
    secret_message.append(list_three[3])

# Create a list in the variable list_five with the 2nd element of list_two, "puppies", and var1 in it in that order
list_five = [list_two[1], "puppies", var1]


# Finally, write a for loop that goes through list five and appends all words that aren't puppies to secret_message
for i in list_five:
    if i != "puppies":
        secret_message.append(i)


# Run this to see if you got it right!
print(secret_message)

# Test Cases 

def test_answer():
    assert len(secret_message) == 8
    assert type(secret_message) == list















               

