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

rmotr_dict.update({  #this will override your current keys but potentially 
                     #add non existing keys 
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



#___________________________________________________________________
# Collections Part 2 


'''
1) Sets

Given a list, remove the duplicates from it, noting that a set always has unique elements. Be sure to return a list as the function's output.

remove_duplicates([5, 6, 1, 1, 1, 7, 7, 2, 6, 5]) #[5,6,1,7,2]
'''
             
def remove_duplicates(target_list):
    return list(set(target_list))

# Test Cases

def test_remove_duplicates_with_occurrences():
    assert remove_duplicates([1, 1, 1, 1, 1, 3, 4, 5, 5, 5]) == [1, 3, 4, 5]



'''
2) Set Operations (Union)

Create a function that will return a set of all elements in at least one of the tuples.

tuple_1 = (1, 5, 6, 4, 8)
tuple_2 = (1, 6, 10, 5)

common_values(tuple_1, tuple_2)  #{1, 4, 5, 6, 8, 10}
'''

def common_values(tuple1, tuple2):
    return set(tuple1) | set(tuple2) #union

# Test Cases

def test_without_repeated_values():
    assert common_values((4, 5, 6, 7), (1, 2, 3)) == {1, 2, 3, 4, 5, 6, 7}

test with repeated values - Run Test

def test_with_repeated_values():
    assert common_values((1, 5, 7, 1, 24), (1, 2, 3, 4)) == {1, 2, 3, 4, 5, 7, 24}



'''
3) Search keys for value

Write a function that receives a dictionary and a value to search for as input. Return a set with all the keys from the dictionary that have that value.

search_keys_for_value({"name" : "Billy", "age" : 12, "fav_num" : 12}, 12)

# {"age", "fav_num"}
'''

def search_keys_for_value(a_dictionary, search_term):
    search_results = []
    for i in a_dictionary:
        if search_term == a_dictionary[i]:
            search_results.append(i)
    return set(search_results)

#OR 

def search_keys_for_value(a_dictionary, search_term):
    result_set = set()
    for key, value in a_dictionary.items():
        if value == search_term:
            result_set.add(key)
return result_set

# Test Cases

def test_search_for_number():
    a_dict = {
        "name": "billy",
        "age": 12,
        "fav_num": 12
    }
    assert search_keys_for_value(a_dict, 12) == {'fav_num', 'age'}

test search for word - Run Test

def test_search_for_word():
    a_dict = {
        1: "hi",
        2: "there",
        3: "easter egg"
    }
    assert search_keys_for_value(a_dict, "easter egg") == {3}

test search not found - Run Test

def test_search_not_found():
    a_dict = {
        "a": "i",
        "b": "love",
        "c": "programming"
    }
    assert search_keys_for_value(a_dict, "howdy") == set()



#___________________________________________________________________
# Quiz week 2


'''
1) Tuple Count

Complete the function tuple_count so that it receives a_tuple and returns a dictionary with a key of each item in the tuple and a value of the count of how many occurrences it has.

tuple_count(('a', 'b', 'a', 'b', 'b', 'c', 'd')) == {
    'b': 3,
    'd': 1,
    'a': 2,
    'c': 1
}
'''

def tuple_count(a_tuple):
    count = {}
    for letter in a_tuple:
        count.setdefault(letter, 0) #create default value for given key 
        count[letter] += 1
    return count
    
# Test Cases 

def test_tuple_count_with_values():
    assert tuple_count(('a', 'a', 'b', 'b', 'b', 'c', 'd')) == {'b': 3, 'd': 1, 'a': 2, 'c': 1}

def test_tuple_count_empty():
    assert tuple_count(tuple()) == {}



'''
2) Analyze String

Write a function that takes a large string, cleans it up and breaks it into individual words, counts how many times each word is used, and then returns a list of words that are repeated.

That sounds like a lot of things, so break it up into two functions and simplify the problem.

Complete the functions count_words so that it receives a_string as an input and processes the string so it becomes a list of words. Then return a dictionary with a each word in the list as a key and how many times that word is repeated (the count) as the value.

Then complete the function get_list_of_duplicates that receives that word count dictionary and returns a SORTED list of each of the items in it that are repeated more than once.

We need to sort the final list answer because dictionaries are unordered and lists are ordered, so when we are creating our list it will likely be created in a different order each run.

string = """Happy Python Programming Programming Programming Happy Me"""

count_words(string) == {"Me": 1, "Python": 1, "Programming": 3, "Happy": 2}
get_list_of_duplicates({"Me": 1, "Python": 1, "Programming": 3, "Happy": 2}) == ["Happy", "Programming"]
'''

def count_words(a_string):
    split_string = a_string.split()
    word_count = {}
    for word in split_string:
        word_count.setdefault(word, 0)
        word_count[word] += 1 
    return word_count 


def get_list_of_duplicates(word_count_dict):
    copy_list = [word for word, count in word_count_dict.items() if count > 1]
    return sorted(copy_list)

# Test Cases 

def test_dictionary_with_count():
    string = """Happy Python Programming Programming Programming Happy Me"""

    assert count_words(string) == {"Me": 1, "Python": 1, "Programming": 3, "Happy": 2}

def test_list_of_duplicates():
    string = """Happy Python Programming Programming Programming Happy Me"""

    result = ["Happy", "Programming"]

    assert get_list_of_duplicates(count_words(string)) == result



'''
3) Sum of Dict Values

Write a function sum_of_dict_values that receives 3 dictionaries as parameters: d1, d2, and d3. Get the sum of the values for each matching key 3 dictionaries, and return a new dictionary showing the results of each. If there is a non-integer as a value, set the value to None for that key.

Example:

Add all the values with the key 'a' together, and you get the sum 22.

d1 = {
    'a': 10,
    'b': 30,
    'c': 5
}

d2 = {
    'a': 7,
    'b': 22,
    'c': 90
}

d3 = {
    'a': 5,
    'b': 1,
    'c': 'hello'
}

result == {
    'a': 22,
    'b': 53,
    'c': None  # d3 has an invalid value, can't be handled
}

sum_of_dict_values(d1, d2, d3) == result
'''
#both belowfuncitons combine to yield accurate result 
def individual_dictionary_process(original_dict, final_dict):
    for key, value in original_dict.items():
        if type(value) != int:
            final_dict[key] = None
        else:
            final_dict.setdefault(key, 0)
            final_dict[key] += value 
        
def sum_of_dict_values(d1, d2, d3):
    final_dict = {}
    individual_dictionary_process(d1, final_dict)
    individual_dictionary_process(d2, final_dict)
    individual_dictionary_process(d3, final_dict)
    return final_dict

# Test Cases

def test_sum_of_dict_values():
    d1 = {
        'a': 10,
        'b': 30,
        'c': 5
    }

    d2 = {
        'a': 7,
        'b': 22,
        'c': 90
    }

    d3 = {
        'a': 5,
        'b': 1,
        'c': 'hello'
    }

    result = {
        'a': 22,
        'b': 53,
        'c': None
    }

    assert sum_of_dict_values(d1, d2, d3) == result


'''
4) Saving the Largest Value

Write a function get_largest_numbers that receives 3 dictionaries as parameters: d1, d2, and d3. Get the highest integer value for each dictionary, and return a new dictionary showing the results of each. If there is a non-integer as a value, ignore it. If none of the values are integers, set that result value to None. Your keys in your result dictionary will be the name of each dictionary parameter (hardcoded to "d1", "d2", and "d3").

Example:

Add all the values with the key 'a' together, and you get the sum 22.

d1 = {
    'a': 30,
    'b': 10,
    'c': 5
}

d2 = {
    'a': 7,
    'b': 'hi',
    'c': 90
}

d3 = {
    'a': 'aloha',
    'b': 'howdy',
    'c': 'hello'
}

result = {
    'd1': 30,
    'd2': 90,
    'd3': None
}

sum_of_dict_values(d1, d2, d3) == result
'''
#both funcitons combine to yield accurate result 
def largest_number_in_dict(indv_dict):
    largest = None
    for value in indv_dict.values():
        if type(value) == int:
            if largest == None:
                largest = value
            else:
                if value > largest:
                    largest = value 
    return largest 
        
def get_largest_numbers(d1, d2, d3):
    return {'d1': largest_number_in_dict(d1), 'd2': largest_number_in_dict(d2), 'd3': largest_number_in_dict(d3)}
    
# Test Cases

def test_largest_values():
    d1 = {
        'a': 30,
        'b': 10,
        'c': 5
    }

    d2 = {
        'a': 7,
        'b': 'hi',
        'c': 90
    }

    d3 = {
        'a': 'aloha',
        'b': 'howdy',
        'c': 'hello'
    }

    result = {
        'd1': 30,
        'd2': 90,
        'd3': None
    }

    assert get_largest_numbers(d1, d2, d3) == result



'''
5) Censor Your Dictionary

The government wants you to "update" some books (in our case, dictionaries) and remove the words with descriptions including certain words. Write a function censor_dictionary that receives an dictionary named unclean_dictionary and a string flagged_word. If the flagged_word is in the description (value) of a word (key), remove the word (key-value pair) from the dictionary.

Hint:
You can use pop or del to remove key-value pairs.

expressions = {
    "pumped": "I'm so darn excited!",
    "happy": "Yeehaw",
    "agreeable": "darn tootin!"
}

assert censor_dictionary(expressions, "darn") == {"happy": "Yeehaw"}
'''

def censor_dictionary(unclean_dictionary, flagged_word):
    clean_dictionary = {}
    for key, value in unclean_dictionary.items():
        if flagged_word not in value:
            clean_dictionary[key] = value
    return clean_dictionary

#OR the less optimal version using pop 
def censor_dictionary(unclean_dictionary, flagged_word):
    removal_list = []
    for word, description in unclean_dictionary.items():
        if flagged_word in description:
            removal_list.append(word)
    for word in removal_list:
        unclean_dictionary.pop(word)
    return unclean_dictionary

# Test Cases 

def test_censor_dictionary():
    expressions = {
       "pumped": "I'm so darn excited!",
       "happy": "Yeehaw",
       "agreeable": "darn tootin!"
    }

    assert censor_dictionary(expressions, "darn") == {
        "happy": "Yeehaw"
    }

