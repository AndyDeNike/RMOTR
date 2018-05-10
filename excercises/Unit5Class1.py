#Unit5/Intro to OOP/Class1

'''
1) Simple class

Create a simple class named SimpleClass. Just that. It should be empty and you should see all the tests pass. Remember that all classes must extend 
from object.
'''

# empty
class SimpleClass(object):
    pass
               
# Test Cases 

def test_object_is_created():
    s = SimpleClass()
    assert isinstance(s, SimpleClass) is True
    assert isinstance(s, object)



'''
2) Simple Attributes

Create an empty class Cookie. Create two instances of it. One of them named cookie1 and the other cookie2. cookie1 should have an attribute scarf with 
the value "green" and cookie2 should have an attribute buttons with the value "blue".
'''

# empty
class Cookie(object):
    pass

cookie1 = Cookie()
cookie2 = Cookie()

cookie1.scarf = 'green'
cookie2.buttons = 'blue'
               
             
# Test Cases

def test_cookie1_attributes():
    assert isinstance(cookie1, Cookie) is True, 'cookie1 is not created'
    assert isinstance(cookie1, object) is True

    assert hasattr(cookie1, 'scarf') is True, "cookie1 doesn't have a scarf attribute"
    assert cookie1.scarf == 'green', "Cookie1's scarf isn't green"

#

def test_cookie2_attributes():
    assert isinstance(cookie2, Cookie) is True, 'cookie2 is not created'
    assert isinstance(cookie2, object) is True

    assert hasattr(cookie2, 'buttons') is True, "cookie2 doesn't have a scarf attribute"
    assert cookie2.buttons == 'blue', "Cookie2's scarf isn't blue"



'''
3) Make Some Cars

Create a class Car and create two instances car1 and car2. Then set three attributes for the instances: color, make, and model. Set whatever value you 
want for those attributes, but make sure they're different from car1 to car2 (i.e. car1 can't have the same color than car2).
'''

# empty
class Car(object):
    pass 

car1 = Car()
car2 = Car()

car1.color = 'Blue'
car1.make = 'Old'
car1.model = '72'

car2.color = 'Green'
car2.make = 'New'
car2.model = '2009'

# Test Cases

def test_car1_attributes():
    assert isinstance(car1, Car) is True, 'car1 is not created'
    assert isinstance(car1, object) is True

    assert hasattr(car1, 'color') is True, "car1 doesn't have a color attribute"

    assert hasattr(car1, 'make') is True, "car1 doesn't have a make attribute"

    assert hasattr(car1, 'model') is True, "car1 doesn't have a model attribute"

#

def test_attributes_are_different():
    assert car1.color != car2.color
    assert car1.make != car2.make
    assert car1.model != car2.model

#

def test_car2_attributes():
    assert isinstance(car2, Car) is True, 'car2 is not created'
    assert isinstance(car2, object) is True

    assert hasattr(car2, 'color') is True, "car2 doesn't have a color attribute"

    assert hasattr(car2, 'make') is True, "car2 doesn't have a make attribute"

    assert hasattr(car2, 'model') is True, "car2 doesn't have a model attribute"



#____________________________________________________________________________



'''
1) Country Methods

In your main module (at the right) we have defined a class Country and we've already created two instances: usa and canada with three attributes for each instance:

    population
    area_in_km2 (in square kilometers)
    gdp (Gross domestic product in dollars)

Your job is to implement the following methods for the Country class:

(Important: Tests are rounding numbers to avoid decimal issues)

Population density
population_density() should return the number of inhabitants per square km. (population / area)

usa.population_density()  # 33.12
canada.population_density()  # 3.52

Dynamic area method

Area can be expressed in different units. These instances have area expressed in square kilometers but you can also use square miles or even Acres or Hectares.

The method area() of the class country should receive an optional parameter unit that can be either: km2, mi2, acres, hectares. By default, units is km2. If the unit passed is invalid (not one in the previous list) it should raise an InvalidAreaUnitException (that you must define). Examples:

usa.area(unit='km2')  # 9833520
usa.area()            # 9833520 (same result, km2 is default)
usa.area(unit='mi2')  #
usa.area(unit='acres')  #
usa.area(unit='hectares')  #

usa.area(unit='INVALID UNIT')  # will raise InvalidAreaUnitException

For simplicity, use the following conversion table (based in km2):

1km2 => 0.3861 mi2
1km2 => 247 acres
1km2 => 100 hectares

GDP per capita
It's not our intention to talk politics, but we want to know how evenly distributed wealth is in each country. Define a method gdp_per_capita() that returns the GDP per capita (gdp / population).

usa.gdp_per_capita()
canada.gdp_per_capita()
'''

class InvalidAreaUnitException(Exception):
    pass

class Country(object):
    # your methods here
    def population_density(self):
        return (self.population/self.area_in_km2)
         
    def area(self, unit='km2'):
        if unit == 'km2':
            return self.area_in_km2
        elif unit =='mi2': 
            return self.area_in_km2 * 0.3861
        elif unit == 'acres':
            return self.area_in_km2 * 247
        elif unit == 'hectares':
            return self.area_in_km2 * 100
        else:
            raise InvalidAreaUnitException('Invalid value')
    
    def gdp_per_capita(self):
        return (self.total_gdp/self.population)

# Test Cases 

def test_area_valid_values():
    assert round(usa.area(unit='km2')) == 9833520
    assert round(usa.area()) == 9833520
    assert round(usa.area(unit='mi2')) == 3796722
    assert round(usa.area(unit='acres')) == 2428879440
    assert round(usa.area(unit='hectares')) == 983352000

    assert round(canada.area(unit='km2')) == 9984670
    assert round(canada.area()) == 9984670
    assert round(canada.area(unit='mi2')) == 3855081
    assert round(canada.area(unit='acres')) == 2466213490
    assert round(canada.area(unit='hectares')) == 998467000

#

def test_population_density():
    assert round(usa.population_density(), 2) == 33.12
    assert round(canada.population_density(), 2) == 3.52

#

def test_gdp_per_capita():
    assert round(usa.gdp_per_capita()) == 62014
    assert round(canada.gdp_per_capita()) == 52231

#

import pytest

def test_area_invalid_unit():
    with pytest.raises(InvalidAreaUnitException):
        usa.area(unit='INVALID')



'''
2) Calculator Method

Create a class Calculator that has two methods add and subtract which receive two numbers and perform the intended operations (returning the value). Example:

c = Calculator()
c.add(2, 5)  # 7
c.subtract(9, 6)  # 3
'''

# empty
class Calculator(object):
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2

# Test Cases 

def test_calculator_add():
    c = Calculator()
    assert c.add(2, 8) == 10

#

def test_calculator_subtract():
    c = Calculator()
    assert c.subtract(7, 2) == 5



'''
3) Make a Car with Attributes

Create a class Car that is initialized by providing three arguments: color, make, and model.

Then, create two instances:
car1 will be have it's color be blue, make be Tesla and model be Model S.
car2 will be have it's color be red, make be Chevy, and model be Camaro.
'''

# empty
class Car(object):
    def __init__(self, color, make, model):
        self.color = color 
        self.make = make
        self.model = model

car1 = Car('blue', 'Tesla', 'Model S')
car2 = Car('red', 'Chevy', 'Camaro')

# Test Cases 


def test_car1_attributes():
    assert isinstance(car1, Car) is True, 'car1 is not created'
    assert isinstance(car1, object) is True

    assert hasattr(car1, 'color') is True, "car1 doesn't have a color attribute"
    assert car1.color == 'blue', "car1's color isn't blue"

    assert hasattr(car1, 'make') is True, "car1 doesn't have a make attribute"
    assert car1.make == 'Tesla', "car1's make isn't Tesla"

    assert hasattr(car1, 'model') is True, "car1 doesn't have a model attribute"
    assert car1.model == 'Model S', "car1's model isn't Model S"

#

def test_car2_attributes():
    assert isinstance(car2, Car) is True, 'car2 is not created'
    assert isinstance(car2, object) is True

    assert hasattr(car2, 'color') is True, "car2 doesn't have a color attribute"
    assert car2.color == 'red', "car2's color isn't red"

    assert hasattr(car2, 'make') is True, "car2 doesn't have a make attribute"
    assert car2.make == 'Chevy', "car2's make isn't Chevy"

    assert hasattr(car2, 'model') is True, "car2 doesn't have a model attribute"
    assert car2.model == 'Camaro', "car2's model isn't Camaro"



'''
4) Make a Car with Doors!

Create a class Car that is initialized by providing one mandatory argument: color.
It will also have one optional/default argument 'number_of_doors' set to be 4 if it is not received as an argument.
'''

# empty
class Car(object):
    def __init__(self, color, number_of_doors=4):
        self.color = color
        self.number_of_doors = number_of_doors

# Test Cases 

def test_default_num_doors():
    car2 = Car(color='green')
    assert isinstance(car2, object) is True

    assert hasattr(car2, 'color') is True
    assert car2.color == 'green'

    assert hasattr(car2, 'number_of_doors') is True
    assert car2.number_of_doors == 4

#

def test_init_attributes():
    car1 = Car(color='blue', number_of_doors=2)

    assert isinstance(car1, object) is True

    assert hasattr(car1, 'color') is True
    assert car1.color == 'blue'

    assert hasattr(car1, 'number_of_doors') is True
    assert car1.number_of_doors == 2



'''
5) Baking Cookies

Create a simple class Cookie that is initialized by providing two arguments: scarf and buttons. The class should initialize the both arguments and also a third one hat that should be None. Example:

c1 = Cookie(scarf='green', buttons='blue')
print(c1.scarf)  # 'green'
print(c1.buttons)  # 'blue'
print(c1.hat)  # None

c2 = Cookie(scarf='yellow', buttons='red')
print(c2.scarf)  # 'yellow'
print(c2.buttons)  # 'red'
print(c2.hat)  # None
'''

class Cookie(object):
    def __init__(self, scarf, buttons, hat=None):
        self.scarf = scarf
        self.buttons = buttons
        self.hat = hat

# Test Cases

def test_init_attributes():
    c1 = Cookie(scarf='green', buttons='blue')
    assert isinstance(c1, object) is True

    assert hasattr(c1, 'scarf') is True
    assert c1.scarf == 'green'

    assert hasattr(c1, 'buttons') is True
    assert c1.buttons == 'blue'

    assert hasattr(c1, 'hat') is True
    assert c1.hat is None



'''
6) Make a Car that can Drive!

Create a class Car that is initialized by providing one mandatory argument: electric.
It will have a method called drive that returns the sound the car makes.
Make sure the text for the sound output matches the example.
You can access the attributes in the drive method from the self variable.

Example:

car1 = Car(electric=False)
print(car1.electric)  # False
print(car1.drive())  # 'VROOOOM'

car2 = Car(electric=True)
print(car2.electric)  # True
print(car2.drive())  # 'WHIRRRRRRR'
'''

class Car(object):
    def __init__(self, electric):
        self.electric = electric

    def drive(self):
        if self.electric:
            return 'WHIRRRRRRR'
        return 'VROOOOM'

# Test Cases 

def test_drive_not_electric():
    car1 = Car(electric=False)
    assert isinstance(car1, object) is True

    assert hasattr(car1, 'electric') is True

    assert car1.electric is False
    assert car1.drive() == 'VROOOOM'

#

def test_drive_electric():
    car2 = Car(electric=True)
    assert isinstance(car2, object) is True

    assert hasattr(car2, 'electric') is True

    assert car2.electric is True
    assert car2.drive() == 'WHIRRRRRRR'



#___________________________________________________________________



'''
1) Temperature Converter

Create a class TempConverter that has two optional parameters celsius 
and fahrenheit. When an object is created, if it receives neither of 
the optional parameters, raise a custom exception 
NoTemperatureException that you will need to create.

You'll need to differentiate which type of temperature you receive when 
you create your object. If the object receives a Celsius temp, store 
it in a variable temp_celsius. If it receives a Fahrenheit temp, 
store it in a variable temp_fahrenheit.

You need two methods:
to_celsius that returns the temperature in Celsius. If a Celsius input 
was received when the object was created, return that. Otherwise 
return the conversion formula (temp_fahrenheit - 32) * 5/9

to_fahrenheit that returns the temperature in Fahrenheit. If a 
Fahrenheit input was received when the object was created, return 
that. Otherwise return the conversion formula (temp_celsius * 9/5) + 32

Look up how to use the round() function on your answers to make them 
only have one decimal place to the right.

Examples:

t = TempConverter(fahrenheit=90)
assert t.to_celsius() == 32.2
assert t.to_fahrenheit() == 90

t = TempConverter(celsius=20)
assert t.to_celsius() == 20
assert t.to_fahrenheit() == 68
'''

class NoTemperatureException(Exception):
	pass

class TempConverter(object):
    def __init__(self, celsius=None, fahrenheit=None):
        if celsius == None and fahrenheit == None:
            raise NoTemperatureException()
        self.temp_celsius = celsius 
        self.temp_fahrenheit = fahrenheit
        
    def to_celsius(self):
        if self.temp_celsius: 
            return self.temp_celsius 
        else:
            return round((self.temp_fahrenheit - 32) * 5/9, 1)
            
    def to_fahrenheit(self):
        if self.temp_fahrenheit:
            return self.temp_fahrenheit
        else:
            return round((self.temp_celsius * (9/5) + 32), 1)

# Test Cases 

import pytest

def test_no_temperature():
    with pytest.raises(NoTemperatureException):
        t = TempConverter()

#

def test_celsius():
    t = TempConverter(celsius=20)
    assert t.to_celsius() == 20
    assert t.to_fahrenheit() == 68

#

def test_fahrenheit():
    t = TempConverter(fahrenheit=90)
    assert t.to_celsius() == 32.2
    assert t.to_fahrenheit() == 90



'''
Lottery Time

Create a class called Lottery with that optionally receives a list 
numbers containing the possible winning numbers. If numbers is not 
received as an optional argument, set it to be a list ranging from 
0-49. When created, your Lottery object should have an attribute 
answer created that is random number from the numbers list.

It needs to have two methods:
- get_answer that returns the answer variable for that object
- play that receives a number and returns True if the number matches 
the answer and False otherwise
'''

# Import here!
import random 

# Define your class here
class Lottery(object):
    def __init__(self, numbers=range(50)):
        self.answer = random.choice(numbers)
        
    def get_answer(self):
        return self.answer 
    
    def play(self, number):
        if number == self.answer:
            return True 
        return False 

# Test Cases 

def test_get_answer():
    l = Lottery(numbers=[9])
    assert l.get_answer() is not None
    assert l.get_answer() == 9

#

def test_random_range():
    l = Lottery()
    assert l.get_answer() is not None
    assert l.play(l.get_answer()) is True

#

def test_play():
    l = Lottery(numbers=[9])
    assert l.play(1) is False
    assert l.play(9) is True

