#Unit4/Exceptions/Class2

'''
1) Breaking Math

Complete the function divide, which takes two parameters a and b and returns the division: a / b. There's one special case: if the parameter b is 0 you should raise a ValueError exception. You could implement it either using a try/except or just an if statement. If you have 2 minutes to spare, try both solutions!

Example:

divide(4, 2)  # 2
divide(8, 2)  # 4
divide(2, 0)  # ValueError Exception raised!
'''

def divide(a, b):
    if b == 0:
        raise ValueError
    return a / b

# Test Cases

def test_division_works():
    assert divide(10, 2) == 5

#

import pytest

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)



'''
2) Parse Number

If you use the input() function, remember how everything entered is received as a string (regardless of if it was a number or not)?

Write a function parse_number to receive a number in string format like '7' and use try/except blocks to try to change its type into an int or a float. If that doesn't work, raise a ValueError.

Examples:

parse_number("3") # 3

parse_number("3.2") # 3.2

parse_number("invalid") # Raises ValueError
'''

def parse_number(number):
    try:
        return int(number)
    except ValueError:
        pass 
    try: 
        return float(number)
    except ValueError:
        pass
    
    raise ValueError

# Test Cases

def test_parse_number_float():
    assert parse_number("3.2") == 3.2

#

import pytest

def test_parse_number_invalid():
    with pytest.raises(ValueError):
        parse_number("invalid")

#

def test_parse_number_integer():
    assert parse_number("3") == 3



'''
3) Reimplement Pop

Sometimes the best ways to get better at coding is to try and recreate features that already exist on your own.

In this exercise, the goal is to replicate the functionality of the dictionary pop method. Write a function pop that receives a dictionary, a key, 
and an optional parameter default_value that is set to None by default.

Using a try/except clause, try and delete the key-value pair in the dictionary, returning the value of the key-value pair if it is successfully 
deleted. If the key is not found and there is a default_value, return default_value. Otherwise, raise a KeyError.
'''

def pop(dictionary, key, default_value=None):
    try: 
        pop_save =  dictionary[key]
        del(dictionary[key])
        return pop_save
    except KeyError:
        if default_value:
            return default_value
        raise KeyError 

# Test Cases

test_dict = {
    "cat": "hat",
    "dog": "log",
    "elf": "shelf"
}


def test_invalid_key_default():
    assert pop(test_dict, "horse", "crickets") == "crickets"
    assert len(test_dict) == 3

#

test_dict = {
    "cat": "hat",
    "dog": "log",
    "elf": "shelf"
}

expected = {
    "cat": "hat",
    "elf": "shelf"   
}

def test_valid_key():
    assert pop(test_dict, "dog") == "log"
    assert len(test_dict) == 2
    assert test_dict == expected

#

import pytest


test_dict = {
    "cat": "hat",
    "dog": "log",
    "elf": "shelf"
}


def test_invalid_key_no_default():
    with pytest.raises(KeyError):
        pop(test_dict, "horse")



'''
4) Parse Date

Complete the function parse_dates built to parse a date_string in 5 different acceptable formats (see examples below), parses it, and returns a datetime object of that date.

Use try/except clauses to try and parse the dates in each format and if none of them work, raise a ValueError.

Hint: You'll need to use datetime.strptime to do this one.

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

Helpful strptime formatting codes:

%B = Full Month Name
%d = 2-digit Day Number for the Month
%Y = 4-digit Year
%y = 2-digit Year
%A = Full Weekday Name
%a = Abbreviated Weekday Name

To do this, you'd do something like the following in your code:

date_string = 'Mon January 03, 2018'
format = '%a %B %d, %Y'

datetime.strptime(date_string, format) # datetime(2018, 1, 3)

You'll need to use the formatting codes to figure out all 5 of the possible date formats. Make sure you cover all 5 formats used as parameters in the examples below.

Examples:

parse_dates('Mon January 03, 2018') # datetime(2018, 1, 3)

parse_dates('Monday January 03, 2018') # datetime(2018, 1, 3)

parse_dates('Monday 03 of January, 2018') # datetime(2018, 1, 3)

parse_dates('January 03, 18') # datetime(2018, 1, 3)

parse_dates('January 03, 2018') # datetime(2018, 1, 3)

parse_dates('INVALID DATE') # Raises ValueError
'''

from datetime import datetime


def parse_dates(date_string):
    parse_formats = [
        '%a %B %d, %Y',
        '%A %B %d, %Y',
        '%A %d of %B, %Y',
        '%B %d, %y',
        '%B %d, %Y'
        ]
    for format in parse_formats:
        try: 
            return datetime.strptime(date_string, format)
        except:
            print('no')
    raise ValueError('Invalid Date Format')

# Test Cases 

def test_format_day_of_week_european_format():
    assert parse_dates('Monday 03 of January, 2018') == datetime(2018, 1, 3)

#

def test_format_day_of_week_regular_format():
    assert parse_dates('Monday January 03, 2018') == datetime(2018, 1, 3)

#

def test_format_month_day_full_year():
    assert parse_dates('January 03, 2018') == datetime(2018, 1, 3)

#

import pytest


def test_invalid_fomat():
    with pytest.raises(ValueError):
        parse_dates('INVALID DATE')

#

def test_format_day_of_week_abbreviated_regular_format():
    assert parse_dates('Mon January 03, 2018') == datetime(2018, 1, 3)

#

def test_format_month_day_decade_year():
    assert parse_dates('January 03, 18') == datetime(2018, 1, 3)



'''
5) Nice Moves

Complete the function validate_tic_tac_toe_move that receives inputs symbol, position_x, and position_y for a move in Tic Tac Toe and checks to make sure each of them are valid.

There are no builtin python exceptions that describe these exceptions meaningfully if one of these move inputs are invalid, so you'll need to create two custom exceptions: InvalidSymbolException and InvalidPositionException.

Remember, all you have to do to create a custom exception is the following:

class ExceptionNameHere(Exception):
    pass

You'll learn more about what the keywords class and Exception mean later. You leave the keyword pass in because all we need to do is raise the exception.

For this function, do the following:
Raise InvalidSymbolException if the symbol is not an 'X' or 'O'
Raise InvalidPositionException if the position_x or position_y are not 0, 1, or 2.

Examples:

validate_tic_tac_toe_move('J', 0, 1) # Raises InvalidSymbolException
validate_tic_tac_toe_move('X', 0, 4) # Raises InvalidPositionException
validate_tic_tac_toe_move('X', 7, 0) # Raises InvalidPositionException
validate_tic_tac_toe_move('O', 1, 2) # Does not raise any exceptions
'''

# Define InvalidSymbolException here
class InvalidSymbolException(Exception):
    pass

# Define InvalidPositionException here
class InvalidPositionException(Exception):
    pass 


def validate_tic_tac_toe_move(symbol, position_x, position_y):
    possible_positions = [0, 1, 2]
    if symbol not in ('X', 'O'):
        raise InvalidSymbolException
    if position_x not in possible_positions or position_y not in possible_positions:
        raise InvalidPositionException

# Test Cases 

import pytest


def test_invalid_position_y():
    with pytest.raises(InvalidPositionException):
        validate_tic_tac_toe_move('X', 0, 4)

#

import pytest


def test_invalid_position_x():
    with pytest.raises(InvalidPositionException):
        validate_tic_tac_toe_move('X', 5, 0)

#

import pytest


def test_invalid_symbol():
    with pytest.raises(InvalidSymbolException):
        validate_tic_tac_toe_move('J', 0, 1)



'''
6) Healthy Recipes Only

Complete the function recipe_calculator so that it receives a list of recipe ingredients that have calories and a sweetness rating associated with each of them in the dictionaries in your main.py file.

Add up the total sweetness of all the items in the recipe and if they exceed a total sweetness of 8, raise a custom exception TooSweetException.

Then add up the total calories of all the items in the recipe and if they exceed a calorie total of 800, raise a custom exception TooManyCalsException.

If the recipe does not raise an exception, return a tuple of (total_sweetness, total_calories).

ingredients = [
    UNIT_OF_EGG,
    UNIT_OF_FLOUR,
    UNIT_OF_WATER,
    UNIT_OF_EGG,
    UNIT_OF_BUTTER
]

recipe_calculator(ingredients) # (2, 450)

ingredients = [
    UNIT_OF_BACON,
    UNIT_OF_BUTTER,
    UNIT_OF_BUTTER,
    UNIT_OF_EGG,
    UNIT_OF_EGG,
    UNIT_OF_EGG
]

recipe_calculator(ingredients) # Raises TooManyCalsException


'''
   
# Define TooSweetException here
class TooSweetException(Exception):
    pass

# Define TooManyCalsException here
class TooManyCalsException(Exception):
    pass 


def recipe_calculator(ingredients):
    """Calculates sweetness and calories of a recipe"""
    total_sweet = 0 
    total_cals = 0
    for ingredient in ingredients:
        total_sweet += ingredient['sweetness']
        total_cals += ingredient['calories']
    if total_sweet > 8:
        raise TooSweetException('Too sweet son!')
    if total_cals > 800:
        raise TooManyCalsException('This many cals will lead to your death')
    return (total_sweet, total_cals)


# Don't delete this!
UNIT_OF_CHOCOLATE = {
    'name': 'Chocolate',
    'calories': 300,
    'sweetness': 2
}

UNIT_OF_SUGAR = {
    'name': 'Sugar',
    'calories': 200,
    'sweetness': 4
}

UNIT_OF_BUTTER = {
    'name': 'Butter',
    'calories': 250,
    'sweetness': 1
}

UNIT_OF_WATER = {
    'name': 'Water',
    'calories': 0,
    'sweetness': 0
}

UNIT_OF_FLOUR = {
    'name': 'Flour',
    'calories': 100,
    'sweetness': 1
}

UNIT_OF_EGG = {
    'name': 'Egg',
    'calories': 50,
    'sweetness': 0
}

UNIT_OF_BACON = {
    'name': 'Bacon',
    'calories': 350,
    'sweetness': 3
}               

# Test Cases 

def test_recipe_good():
    ingredients = [
        UNIT_OF_EGG,
        UNIT_OF_FLOUR,
        UNIT_OF_WATER,
        UNIT_OF_EGG,
        UNIT_OF_BUTTER
    ]
    assert recipe_calculator(ingredients) == (2, 450)

#

import pytest


def test_recipe_is_too_sweet():
    ingredients = [
        UNIT_OF_CHOCOLATE,
        UNIT_OF_SUGAR,
        UNIT_OF_SUGAR,
        UNIT_OF_SUGAR,
        UNIT_OF_BUTTER
    ]
    with pytest.raises(TooSweetException):
        recipe_calculator(ingredients)

#

import pytest


def test_recipe_too_many_cals():
    ingredients = [
        UNIT_OF_BACON,
        UNIT_OF_BUTTER,
        UNIT_OF_BUTTER,
        UNIT_OF_EGG,
        UNIT_OF_EGG,
        UNIT_OF_EGG
    ]
    with pytest.raises(TooManyCalsException):
        recipe_calculator(ingredients)

