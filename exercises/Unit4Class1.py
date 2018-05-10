#Unit4/Modules and Packages/Class1

'''
1) Get Random List Element

Time to practice using the Standard Library (stdlib)!

Let's start with the random library.

Import the random library and write a function get_random_list_element that receives the list a_list and returns a random element from that list.

Hint: You'll have to look up the documentation to decide which method of the random library to use to solve this assignment.

Examples:

get_random_list_element(["hats", "shoes", "pants", "scarf", "shirt"]) # "shoes"


get_random_list_element(["hats", "shoes", "pants", "scarf", "shirt"]) # "shirt"
'''

# Import the library here!
import random 

def get_random_list_element(a_list):
    return random.choice(a_list)

# Test Cases 

def test_random_element():
    assert get_random_list_element([1, 2, 3, 4, 5]) in [1, 2, 3, 4, 5]



'''
2) Area of Circle

Time for the math library. It has a lot of mathematical methods and numbers. Surprised?

Suppose you wanted to calculate the area of a circle with more precision and you didn't have pi memorized to 100 digits like most people do. You could either start learning about pi... or just use the math library!

Okay... time to make that hypothetical area of a circle program less hypothetical.

Create a function area_of_circle that receives the radius and returns the area of the circle (pi * r * r) using the math library to get your value for pi.

Examples:

area_of_circle(1) #  3.141592653589793

area_of_circle(2) # 12.566370614359172
'''

# Import the library here!
import math 

def area_of_circle(radius):
    return math.pi * radius * radius 

# Test Cases

def test_area_radius_three():
    assert area_of_circle(3) == 28.274333882308138

#

def test_area_radius_one():
    assert area_of_circle(1) == 3.141592653589793



'''
3) Get Variance from List

Perhaps you need to calculate some statistics on data you have.

You COULD write your own code to do this. But you are a strong, confident, successful programmer with a busy schedule and ain't nobody got time for dat (unless you want the practice).

Import the statistics library and write a function get_variance_from_list that receives the list a_list and returns the variance for the numbers in that list using a method from the library.

Note: This particular library only works in python versions 3.4 and greater. Make sure when you run this code you have it set to Python 3 in the platform (button in top right on Learn)!

Examples:

get_variance_from_list([1, 3, 8, 4, 22]) # 71.3
'''

# Import the library here (must be python 3.4+)!
import statistics

def get_variance_from_list(a_list):
    return statistics.variance(a_list)

# Test Cases 

def test_get_variance():
    assert get_variance_from_list([1, 3, 8, 4, 22]) == 71.3



'''
4) Nice Looking Date

Dates and time in Python are stored in a separate data type, the datetime object. The formatting can be a little tricky at first, so it is best to 
practice with it a fair amount to become familiar. Generally, you'll have the documentation handy for reference.

Datetime Documentation

For the first exercise, you'll want to import the date object from datetime library by typing from datetime import date. Then create a function called 
format_date that will receive a datetime object a_date and return a formatted string of the date. To do that, use the strftime method that you'll find 
in the documentation. Return a string of the formatted as below:

Weekday, Month Day Year

Example:

format_date(date(1987, 9, 29)) # "Tuesday, September 29 1987"

strftime info
'''

# Import the library here!
from datetime import date 

def format_date(a_date):
    return a_date.strftime('%A, %B %d %Y')

# Test Cases

def test_date_one():
    assert format_date(date(1964, 7, 31)) == "Friday, July 31 1964"

#

def test_date_one():
    assert format_date(date(1987, 9, 29)) == "Tuesday, September 29 1987"



'''
5) Celebrate if Friday

Now that you are more familiar with formatting dates as strings, it's time to do something with that knowledge.

Make a simple function called celebrate_if_friday that checks a_date that is passed to it and sees if it is Friday. If it is, return a string that says "YES!" and return a string that says "Aww" if not.

Examples:

celebrate_if_friday(date(2018, 1, 5)) # "YES!"

celebrate_if_friday(date(1987, 9, 29)) # "Aww"
'''

# Import the library here!
from datetime import date

def celebrate_if_friday(date):
    if date.strftime('%A') == 'Friday':
        return "YES!"
    return "Aww"

# Test Cases

def test_celebrate():
    assert celebrate_if_friday(date(2018, 1, 5)) == "YES!"

#

def test_dont_celebrate():
    assert celebrate_if_friday(date(1987, 9, 29)) == "Aww"



'''
6) Counting the Days

The datetime library is useful for much more than just getting and formatting dates!

You can let Python perform mathy calculations for you as well.

For this exercise, create a function counting_the_days that receives a variable start_date and end_date. Subtract start_date from end_date and you 
will produce a timedelta object. To practice using this, return your timedelta object in the format of days using they days method.

Example:

counting_the_days(date(1987, 9, 29), date(2017, 9, 29)) # 10958
'''



# Import the library here!
from datetime import date

def counting_the_days(start_date, end_date):
    delta_time = end_date - start_date 
    return delta_time.days

# Test Cases

def test_counting_the_days():
    assert counting_the_days(date(1987, 9, 29), date(2017, 9, 29)) == 10958




