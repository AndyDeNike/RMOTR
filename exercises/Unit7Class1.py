#Unit7/Functional Programming/Class1

'''
1) 
Sum Multiple Terms

Write a function that receives multiple arguments and returns the sum of 
them. Example:

sum_multiple(2, 3, 5, 7) == 17
sum_multiple(2, 3) == 5

If no arguments are provided, an Exception should be raised. Check the 
test cases for the complete spec.
'''

def sum_multiple(*args):
    if not args:
        raise AttributeError()
    return sum(args)

# Test Cases 

def test_sum_multiple_terms():
    assert sum_multiple(2, 3) == 5
    assert sum_multiple(2, 3, 5, 7) == 17

#

import pytest

def test_sum_with_no_elements_raises_error():
    with pytest.raises(AttributeError):
        sum_multiple()



'''
2) 
Divisible numbers comprehension

Write a function that receives a list of numbers and a term 'n' and returns only the elements that are divisible by that term 'n'. You must use List comprehensions to solve it.

divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)  == [9, 6, 3]
'''

def divisible_numbers(a_list, term):
    return [x for x in a_list if x % term == 0]

#

def test_many_divisible_number():
    assert divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3) == [9, 6, 3]

#

def test_empty_list():
    assert divisible_numbers([], 2) == []

#

def test_no_result():
    assert divisible_numbers([2, 4, 8], 5) == []



'''
3) Square elements using list comprehensions

Write a function that receives a list of integers and returns a list with all the elements squared using list comprehensions.

square_elements([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
'''

def square_elements(a_list):
    return [x**2 for x in a_list]

# Test Cases 

def test_square_elements_repeated():
    square_elements([1, 1, 2, 2, 3, 3]) == [1, 1, 4, 4, 9, 9]

#

def test_square_elements_empty_list():
    square_elements([]) == []

#

def test_square_elements():
    square_elements([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]



'''
4) Even numbers using list comprehensions

Write a function that receives a list of numbers and returns only the even elements. You must use List comprehensions to solve it.

even_numbers([5, 4, 3, 2, 1]) == [4, 2]
'''

def even_numbers(a_list):
    return [x for x in a_list if x%2 == 0]

# Test Cases 

def test_empty_list_even_numbers():
    assert even_numbers([]) == []

#

def test_no_even_numbers():
    assert even_numbers([5, 3, 7, 9, 1]) == []

#

def test_multiple_even_numbers():
    assert even_numbers([5, 4, 3, 2, 1]) == [4, 2]

#

def test_one_even_numbers():
    assert even_numbers([5, 4, 3, 7, 9, 1]) == [4]



'''
5) Temperature Conversion Using list comprehensions

Write a function that combines list comprehensions and lambdas to transform temperatures given in celsius to fahrenheit.

to_fahrenheit([0, 10, 25, 30, 100]) == [32.0, 50.0, 77.0, 86.0, 212.0]
'''

def to_fahrenheit(a_list):
	#clean below 
    #return [(x * 1.8 + 32.0) for x in a_list]
    return [(lambda x: x * 1.8 + 32.0)(x) for x in a_list]

# Test Cases 

def test_to_fahrenheit_repeated_values():
    assert to_fahrenheit([0, 10, 10, 100]) == [32.0, 50.0, 50.0, 212.0]

#

def test_to_fahrenheit_empty_list():
    assert to_fahrenheit([]) == []

#

def test_to_fahrenheit():
    assert to_fahrenheit([0, 10, 25, 30, 100]) == [32.0, 50.0, 77.0, 86.0, 212.0]



'''
6) Divisible numbers comprehension with multiple terms

Write a function that receives a list of numbers and a list of terms 
and returns only the elements that are divisible by ALL the terms. You 
must use two nested list comprehensions to solve it.

divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3]) == 
				  [12, 6]

Warning, this assignment is difficult. If you get stuck, try working it 
with a for-loop first and then start turning it into list comprehensions.
'''

def divisible_numbers(a_list, a_list_of_terms):
    return [num for num in a_list 
           if all([num % term == 0 for term in a_list_of_terms])]
    
    #opitonal with len()
    #return [num for num in a_list 
    	   #if len([1 for term in a_list_of_terms if num%term == 0]) == 
    	   #len(a_list_of_terms)]

# Test Cases

def test_empty_list():
    assert divisible_numbers([], [5, 7]) == []

#

def test_many_divisible_numbers():
    result = divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])
    expected = [12, 6]

    assert result == expected

#

def test_no_result():
    assert divisible_numbers([2, 4, 8], [5, 7]) == []

#

def test_one_divisible_numbers():
    result = divisible_numbers([16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4])
    assert  result == [12]

#

def test_both_empty_lists():
    assert divisible_numbers([], []) == []




