#Unit2/Collections Part 2/Class2

'''
1) Add Python to Dict

Write a function that receives a dictionary as input, adds a new key-value pair saying "fav_language": "python" to it, and returns it! :D

add_to_dictionary({"first_name": "jon", "last_name": "snow"})

# {
#   "first_name": "jon",
#   "last_name": "snow",
#   "fav_language": "python"
# }
'''

def add_to_dictionary(a_dictionary):
    a_dictionary['fav_language'] = 'python'
    return a_dictionary 

# Test Cases

def test_overwrite_existing_key():
    assert add_to_dictionary({
        "fav_language": "elvish"
    }) == {
        "fav_language": "python"
    }

def test_add_new_key_to_dictioanry():
    original = {
        "first_name": "jon",
        "last_name": "snow"
    }
    expected = {
        "first_name": "jon",
        "last_name": "snow",
        "fav_language": "python"
    }
    assert add_to_dictionary(original) == expected



'''
2) Updating a Dictionary

Update the dictionary provided in the editor making the following changes:

    Update the name from "RMOTR" to "rmotr.com"
    Include a new key email with the value 'questions@rmotr.com'
    Update the list of courses to include "Django Web Development"
'''

rmotr_dict = {
    'name': 'RMOTR',
    'courses': ['Intro to Python', 'Advanced Pyhton'],
}

rmotr_dict.update({  #this will override your current keys
    'name' : 'rmotr.com',
    'email' : 'questions@rmotr.com',
    'courses' : ['Intro to Python', 'Advanced Pyhton', 'Django Web Development']
})

# Test Cases 

def test_django_is_in_courses_list():
    assert rmotr_dict['courses'] == ['Intro to Python', 'Advanced Pyhton', 'Django Web Development']

def test_email_is_correct():
    assert rmotr_dict['email'] == 'questions@rmotr.com'

def test_name_is_updated():
    assert rmotr_dict['name'] == 'rmotr.com'




'''
3) Banana Dictionary

Write a function that receives a number X and creates a dictionary containing X elements. The elements will be the word "banana"*X and the number. If the number passed to the function is less than 1, return an empty dictionary.

banana_dict(2)
{
  "banana": 1,
  "bananabanana": 2
}

banana_dict(4)
{
  "banana": 1,
  "bananabanana": 2,
  "bananabananabanana": 3,
  "bananabananabananabanana": 4
}
'''

def banana_dict(num):
    banana_dict = {}
    if num >= 1:
        for i in range(num):
            banana_dict['banana' * (i + 1) ] = i + 1
    return banana_dict

# Test Cases

def test_dictionary_with_zero_elements():
    assert banana_dict(0) == {}

def test_dictionary_with_one_element():
    assert banana_dict(1) == {'banana': 1}

def test_dictionary_with_three_elements():
    assert banana_dict(3) == {
        'banana': 1,
        'bananabanana': 2,
        'bananabananabanana': 3
    }




'''
4) Largest key

Write a function that receives a dictionary with only String keys and 
returns the longest key in the dictionary. Example:

longest_key({'hello': 'World', 'abc': 123})  # hello
longest_key({})  # None
'''

def longest_key(a_dict):
    longest = None
    for i in a_dict:
        if not longest or len(i) > len(longest):
            longest = i 
    return longest

# Test Cases 

def test_one_item():
    assert longest_key({'rmotr': 'Intro to Python'}) == 'rmotr'

def test_with_no_items():
    assert longest_key({}) == None

def test_with_many_items():
    assert longest_key({'abcd': 'XXYYZZ', 'ac': 'MMM'}) == 'abcd'



'''
5) Dict to Tuple

Create a function dict_to_tuple that receives a dictionary and returns a list of tuples containing the key-value pairs. Example:

dict_to_tuple({'a': 1, 'b': 2})  # [('a', 1), ('b', 2)]
dict_to_tuple({'Hello': 'World'})  # [('Hello', 'World')]
'''
#optimal list comprehension 
def dict_to_tuple(a_dict):
    return [(k, v) for k, v in a_dict.items()]
#OR

def dict_to_tuple(a_dict):
    return list(a_dict.items())

#OR
    
def dict_to_tuple(a_dict):
    tuplist = []
    for k, v in a_dict.items():
        tuplist.append((k, v))
    return tuplist

# Test Cases

def test_empty_dict():
    assert dict_to_tuple({}) == []

def test_one_item_dict():
    result = dict_to_tuple({'my_key': 20})
    expected = [('my_key', 20)]
    assert result == expected

def test_with_many_items():
    result = dict_to_tuple({'Z': 3, 'X': 2, 'Y': 1})
    expected = [('Z', 3), ('X', 2), ('Y', 1)]
    assert sorted(result) == sorted(expected)



'''
6) Write a function that inverts a dictionary's keys and values so that all values are now keys, and that all keys are now values.

a_dict = {1: 'a', 2: 'b', 3:'c'}

invert_dict(a_dict) # {'a': 1, 'b': 2, 'c': 3}
'''

def invert_dict(target_dict):
    rev_dict = {}
    for k, v in target_dict.items():
        rev_dict[v] = k
    return rev_dict

#optimal dict comprehension 
def invert_dict(target_dict):
    return {v: k for k, v in target_dict.items()}

# Test Cases

def test_invert_empty_dict():
    assert invert_dict({}) == {}

def test_invert_one_element_dict():
    assert invert_dict({1: 'a'}) == {'a': 1}

def test_invert_many_elements_dict():
    assert invert_dict({
        1: 'a', 2: 'b',
        3: 'c', 4: 'd',
        5: 'e'
    }) == {
        'a': 1, 'b': 2,
        'c': 3, 'd': 4,
        'e': 5
    }



'''
7) Count Occurrences

Write a function that receives a list as input and returns a dictionary that counts how many times the data in the list is repeated.

count_occurrences(["a", "b", "c", "a", "a," "b"])

# {"a" : 3, "b" : 2, "c": 1}
'''

def count_occurrences(a_list):
    count_list = {}
    for i in a_list:
        if i not in count_list:
            count_list[i] = 1
        else: 
            count_list[i] += 1 
    return count_list 
    
# Test Cases 

def test_count_occurrences_not_unique():
    assert count_occurrences(["a", "b", "c", "a", "a", "b"]) == {
        "a": 3,
        "b": 2,
        "c": 1
    }

def test_count_occurrences_with_numbers():
    assert count_occurrences([12, 42, 42]) == {42: 2, 12: 1}

def test_count_occurrences_all_unique():
    assert count_occurrences(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


        





               

