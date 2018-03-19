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






               

