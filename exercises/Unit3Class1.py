#Unit3/Collections Part 3/Class1

'''
1) Create ASCII Box

Write a function create_box that takes three inputs: height (rows), width (columns), and a character char and creates a height × width box using the character char.

For this exercise, it's recommended to use a nested for-loop. There are other ways of solving it (which might be a good starting point), but try reaching the nested for-loop solution.

>>> create_box(3, 4, '*')
'****
 ****
 ****'
>>> create_box(2, 2, '@')
'@@
 @@'

IMPORTANT: You need to return your box, not just print it.
'''

def create_box(height, width, char):
    box = ''
    for i in range(height):
        box += width * char + "\n"
    return box

# Test Cases 


box_1x1_expected = """
@
""".lstrip()

def test_a_1x1_box():
    assert create_box(1, 1, '@') == box_1x1_expected

#

box_5x8_expected = """
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
""".lstrip()

def test_a_5x8_box():
    assert create_box(5, 8, 'x') == box_5x8_expected

#

box_3x4_expected = """
****
****
****
""".lstrip()

def test_a_3x4_box():
    assert create_box(3, 4, '*') == box_3x4_expected



'''
2) Create Empty Box

Expand on the last assigment and write a function create_empty_box that
takes three inputs: height (rows), width (columns), and a character 
char and creates a height × width box using the character char that only
has characters on the borders of the box (it's not filled in).

If the box height or width are less than 3, return 'Invalid box 
dimensions' because it won't be an empty box.

Hint: Look for patterns in the the way the empty box looks when you 
design your solution (top to bottom, side to side).
'''

def create_empty_box(height, width, char):
    if height < 3 or width < 3:
        return 'Invalid box dimensions'
    empty_box = "" #empty string
    empty_box += width * char + '\n' #top
    for i in range(height-2):
        empty_box += char + (" " * (width - 2)) + char + '\n' #everything not top/bottom
    empty_box += width * char + '\n' #bottom
    return empty_box 

# Test Cases

def test_invalid_box_height():
    assert create_empty_box(1, 4, 'Y') == "Invalid box dimensions"

#

box_5x8_expected = """
xxxxxxxx
x      x
x      x
x      x
xxxxxxxx
""".lstrip()

def test_a_5x8_box():
    assert create_empty_box(5, 8, 'x') == box_5x8_expected

#

box_3x4_expected = """
****
*  *
****
""".lstrip()

def test_a_3x4_box():
    assert create_empty_box(3, 4, '*') == box_3x4_expected

#

def test_invalid_box_width():
    assert create_empty_box(3, 1, '$') == "Invalid box dimensions"



'''
3) Nested Pyramid

Write a function nested_pyramid that receives a number height and a 
character char and builds an ASCII Pyramid with them. 
'''

def nested_pyramid(height, char):
    pyramid = ""
    for i in range(1, height+1):
        pyramid += i * char + '\n'
    return pyramid

# Test Cases

pyramid_5_expected = """
#
##
###
####
#####
""".lstrip()


def test_pyramid_with_5_levels():
    assert nested_pyramid(5, '#') == pyramid_5_expected

#

pyramid_3_expected = """
@
@@
@@@
""".lstrip()


def test_pyramid_with_3_levels():
    assert nested_pyramid(3, '@') == pyramid_3_expected



'''
4) Advanced Nested Pyramids

Extend your previous solution to include a third parameter "order" 
which can be either "ASC" or "DESC. Depending of the order provided, 
the pyramid will be displayed in ascending order ("ASC") or descending 
order ("DESC"). 
'''

def advanced_nested_pyramid(height, char, order):
    pyramid = ""
    if order == 'ASC':
        for i in range(1, height+1):
            pyramid += char * i + '\n'
    elif order == 'DESC':
        for i in range(height, 0, -1):
            pyramid += char * i + '\n'
    return pyramid 

# Test Cases

desc_pyramid = """
xxxxxxx
xxxxxx
xxxxx
xxxx
xxx
xx
x
""".lstrip()


def test_descending_pyramid():
    assert advanced_nested_pyramid(7, 'x', 'DESC') == desc_pyramid

#

pyramid_5_expected = """
#
##
###
####
#####
""".lstrip()


def test_ascending_pyramid():
    assert advanced_nested_pyramid(5, '#', 'ASC') == pyramid_5_expected



'''
5) Identity Matrix

An identity matrix is defined in the following way:

image

Basically, all the elements in the diagonal are ones (1s) and the rest 
are zeros (0s).

An identity matrix has a size associated. For example, this is an 
identity matrix of size 3:

1 0 0
0 1 0
0 0 1

And this is a matrix of size 5:

1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1

A matrix is represented, Pythonically, with a "list of lists". 
Example:

# size 3
size_3_matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
# size 5
size_5_matrix = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

Write a function identity_matrix that receives a size parameter and 
builds an identity matrix using "lists of lists".
'''

def identity_matrix(size):
    id_matrix = []
    for i in range(size):
        id_matrix.append([])
        for idx in range(size):
            if idx == i:
                id_matrix[i].append(1)
            else: 
                id_matrix[i].append(0)
    return id_matrix

# Test Cases

size_5_matrix = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

def test_size_5_identity_matrix():
    assert identity_matrix(5) == size_5_matrix

#

size_2_matrix = [
    [1, 0],
    [0, 1],
]

def test_size_2_identity_matrix():
    assert identity_matrix(2) == size_2_matrix

#

size_3_matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]

def test_size_3_identity_matrix():
    assert identity_matrix(3) == size_3_matrix



'''
6) Random Numbers Matrix

Use the random module (more below) to write a function random_matrix that returns a matrix size m × n with random numbers (m is the number of rows and n is the number of columns).
The only restriction is that elements in the matrix CAN'T be repeated, they must be unique. Examples:

random_matrix(3, 2)
[
    [29, 11],
    [91, 85],
    [56, 18],
]

random_matrix(4, 4)
[
    [29, 11, 23, 90],
    [91, 85, 92, 75],
    [56, 18, 13, 47],
    [65, 99, 49, 10]
]
'''

import random

def random_matrix(m, n):
    matrix = []
    repeated = []
    for i in range(m): #rows 
        matrix.append([]) #add a list for each row ('m')
        for j in range(n): #columns
            random_num = random.randint(0, 100)
            while random_num in repeated:
                random_num = random.randint(0,100)
            repeated.append(random_num)
            matrix[i].append(random_num)
    return matrix

# Test Cases

def test_size_3x2_elements_not_repeated():
    matrix = random_matrix(3, 2)

    assert len(matrix) == 3
    for row in matrix:
        assert len(row) == 2

    repeated_elements = []
    for row in matrix:
        for elem in row:
            assert elem not in repeated_elements
            repeated_elements.append(elem)



'''
7) Zip two collections

IMPORTANT: For this assignment you CAN'T use the builtin zip function.

For this assignment, we'll rewrite the builtin function zip, it's going 
to be called rmotr_zip. rmotr_zip receives two collections (lists, tuples, 
doesn't matter) and must "zip" their elements. Zip just means matching elements in the same positions for both collections. A conceptual example of zip:

collection_a = ['A', 'B', 'C', 'D']
collection_b = [ 1 ,  2 ,  3 ,  4 ]

# Zip collection_a and collection_b means:

'A' => 1
'B' => 2
'C' => 3
'D' => 4

The result is a list containing tuples for each new pair. Example of 
the rmotr_zip function:

result = rmotr_zip(['A', 'B', 'C'], [1, 2, 3])

# The following formatting doesn't change anything
# It's just for readability purposes
result == [
  ('A', 1),
  ('B', 2),
  ('C', 3),
]

# A few more examples
rmotr_zip([1, 1, 1], [2, 2, 2])  # [(1, 2), (1, 2), (1, 2)]
rmotr_zip(['a', 'b'], [1, 2, 3])  # None! Different number of elements
'''

def rmotr_zip(collection_a, collection_b):
    if len(collection_a) != len(collection_b):
        return None
    zip_result = []
    for i in range(len(collection_a)):
        zip_result.append((collection_a[i], collection_b[i]))
    return zip_result 

# Test Cases 

def test_with_many_elements():
    result = rmotr_zip(['A', 'B', 'C'], [1, 2, 3])
    expected = [
      ('A', 1),
      ('B', 2),
      ('C', 3),
    ]

    assert result == expected

#

def test_with_different_elements():
    assert rmotr_zip(['A', 'B'], [1]) == None

#

def test_with_one_element():
    assert rmotr_zip(['A'], [1]) == [('A', 1)]



'''
8) Number of customers per state

Customers are expressed as a dictionary, divided by state. Each key represents a state. Example:

customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',
        'age': 31
    }, {
        'name': 'Robert',
        'age': 16
    }],
    'NY': [{
        'name': 'Linda',
        'age': 71
    }],
    'CA': [{
        'name': 'Barbara',
        'age': 15
    }, {
        'name': 'Paul',
        'age': 18
    }]
}

Each state contains a list with all the customers. A single customer is represented as a dictionary with only two keys, name and age.

Write a function number_of_customers_per_state that receives a customers dictionary and calculates the number of customers per state. The result will be a new dictionary, with each key containing a state and the count as the associated value.

Example:

customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',
        'age': 31
    }, {
        'name': 'Robert',
        'age': 16
    }],
    'NY': [{
        'name': 'Linda',
        'age': 71
    }],
    'CA': [{
        'name': 'Barbara',
        'age': 15
    }, {
        'name': 'Paul',
        'age': 18
    }]
}
result = number_of_customers_per_state(customers)
print(result)

Prints:

expected_result = {
    'UT': 3,
    'NY': 1,
    'CA': 2
}
'''

def number_of_customers_per_state(customers_dict):
    state_count = {} 
    for state in customers_dict:
        state_count.setdefault(state, 0)
        if customers_dict[state] != None:
            state_count[state] = len(customers_dict[state])
    return state_count

# Test Cases

def test_number_of_customers_per_state():
    """Should return the correct number of customers per state."""
    customers = {
        'UT': [{
            'name': 'Mary',
            'age': 28
        }, {
            'name': 'John',
            'age': 31
        }, {
            'name': 'Robert',
            'age': 16
        }],
        'NY': [{
            'name': 'Linda',
            'age': 71
        }],
        'CA': [{
            'name': 'Barbara',
            'age': 15
        }, {
            'name': 'Paul',
            'age': 18
        }]
    }
    expected_result = {
        'UT': 3,
        'NY': 1,
        'CA': 2
    }
    assert number_of_customers_per_state(customers) == expected_result

#

def test_number_of_customers_per_state_with_blank_state():
    """Should return the correct number of customers per state."""
    customers = {
        'UT': [{
            'name': 'Mary',
            'age': 28
        }, {
            'name': 'John',
            'age': 31
        }, {
            'name': 'Robert',
            'age': 16
        }],
        'NY': None,  # Be Careful! NY value is None
        'CA': [{
            'name': 'Barbara',
            'age': 15
        }, {
            'name': 'Paul',
            'age': 18
        }]
    }
    expected_result = {
        'UT': 3,
        'NY': 0,
        'CA': 2
    }
    assert number_of_customers_per_state(customers) == expected_result



'''
9) Eldest customer per state

With the same structure as before, now you need to write a function that finds the eldest customer per state. Example:

customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',  # Eldest
        'age': 31
    }, {
        'name': 'Robert',
        'age': 16
    }],
    'NY': [{
        'name': 'Linda',  # Eldest (only customer)
        'age': 71
    }],
    'CA': [{
        'name': 'Barbara',
        'age': 15
    }, {
        'name': 'Paul',
        'age': 18
    }, {
        'name': 'Helen',  # Eldest
        'age': 29
    }]
}
results = eldest_customer_per_state(customers)
print(results)

Prints:

expected_result = {
    'UT': {
        'name': 'John',
        'age': 31
    },
    'NY': {
        'name': 'Linda',
        'age': 71
    },
    'CA': {
        'name': 'Helen',
        'age': 29
    }
}
'''

def eldest_customer_per_state(customers_dict):
    eldest_in_state = {}
    for state, people in customers_dict.items():
        oldest = None
        for individual in people:
            if oldest == None or individual['age'] > oldest['age']:
                oldest = individual
        eldest_in_state[state] = oldest 
    return eldest_in_state

#

def test_eldest_customers_with_states():
    """Should return the eldest customer per state."""
    customers = {
        'UT': [{
            'name': 'Mary',
            'age': 28
        }, {
            'name': 'John',
            'age': 31
        }, {
            'name': 'Robert',
            'age': 16
        }],
        'NY': [{
            'name': 'Linda',
            'age': 71
        }, {
            'name': 'Lisa',
            'age': 25
        }, {
            'name': 'Daniel',
            'age': 45
        }],
        'CA': [{
            'name': 'Barbara',
            'age': 15
        }, {
            'name': 'Paul',
            'age': 18
        }, {
            'name': 'Helen',
            'age': 29
        }]
    }
    expected_result = {
        'UT': {
            'name': 'John',
            'age': 31
        },
        'NY': {
            'name': 'Linda',
            'age': 71
        },
        'CA': {
            'name': 'Helen',
            'age': 29
        }
    }
    assert eldest_customer_per_state(customers) == expected_result

#

def test_eldest_customers_with_empty_states():
    customers = {
        'UT': [{
            'name': 'Mary',
            'age': 28
        }, {
            'name': 'John',
            'age': 31
        }],
        'NY': []
    }
    expected_result = {
        'UT': {
            'name': 'John',
            'age': 31
        },
        'NY': None
    }
    assert eldest_customer_per_state(customers) == expected_result

