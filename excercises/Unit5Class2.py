#Unit5/Intro to OOP/Class2

'''
1) Points and Lines

Time to make things a bit more complicated. Now you need to write two classes!

Create a class Point that receives two parameters x and y and stores them within each point created.

Next create a class Line that receives two points as parameters p1 and p2.

It needs the following 3 methods:
slope that returns the slope of the line based on the two points
Equation: (y2 - y1)/(x2 - x1)
y_intercept that returns the y-intercept of the line
Equation: y1 - (slope * x1)
* formula that returns a string of the formula of the line (if the slope is 1, omit it).
Equation: y = mx + b where m is slope and b is y-intercept

Note: None of these methods receive any external parameters

For the formula string, if the y-intercept can be truncated (e.g. using 1 instead of 1.0), do it using {:g} in your string formatting.

"{b:g}".format(b=3.0) # 3
"{b:g}".format(b=3.2) # 3.2

Example:

p1 = Point(0, 1)
p2 = Point(1, 2)

l = Line(p1, p2)

l.slope() # 1
l.y_intercept() # 1
l.formula() # 'y = x + 1.0'
'''

# Define Point class here
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define Line class here
class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2 
    
    def slope(self):
        return ((self.p2.y - self.p1.y)/(self.p2.x - self.p1.x))
        
    def y_intercept(self):
        return (self.p1.y) - (self.slope() * self.p1.x)
        
    def formula(self):
        if self.slope() == (1 or 1.0):
            return 'y = x + {:g}'.format(self.y_intercept())
        return 'y = {}x + {:g}'.format(self.slope(), self.y_intercept())

# Test Cases 

def test_point():
    p = Point(4, 2)
    assert p.x == 4
    assert p.y == 2

#

def test_line():
    p1 = Point(0, 1)
    p2 = Point(1, 2)

    l = Line(p1, p2)

    assert l.slope() == 1
    assert l.y_intercept() == 1
    assert l.formula() == 'y = x + 1'



'''
2) Cached Calculator

Write a class Calculator that has the same methods as the previous one (add and subtract). But it should also have an attribute cache that keeps track 
of the operations being already performed as a dictionary (see example below and test cases). If the operation was already performed, the method 
should return the value from the cache. Example:

>>> c = Calculator()
>>> c.cache
{}
>>> c.add(2, 3)
5
>>> c.cache
{
  'add': [
    (2, 3, 5)
  ]
}
>>> c.subtract(8, 2)
6
>>> c.cache
{
  'add': [
    (2, 3, 5)
  ],
  'subtract': [
    (8, 2, 6)
  ]
}
>>> c.add(9, 3)
12
>>> c.cache
{
  'add': [
    (2, 3, 5),
    (9, 3, 12)
  ],
  'subtract': [
    (8, 2, 6)
  ]
}
# Same method invoked again:
>>> c.add(2, 3)  # Should be returned from the cache
5
'''

# empty
class Calculator(object):
    def __init__(self, cache={}):
        self.cache = cache 
        
    def add(self, num1, num2):
        if 'add' not in self.cache:
            self.cache['add'] = [(num1, num2, num1+num2)]
            return num1+num2
        else:
            if (num1, num2, num1+num2) in self.cache['add']:
                return num1 + num2
            else:
                self.cache['add'].append((num1, num2, num1+num2))
                return num1 + num2
    def subtract(self, num1, num2):
        #return num1 - num2
        if 'subtract' not in self.cache:
            self.cache['subtract'] = [(num1, num2, num1-num2)]
            return num1-num2
        else:
            if (num1, num2, num1-num2) in self.cache['subtract']:
                return num - num2
            else:
                self.cache['subtract'].append((num1, num2, num1-num2))
                return num1 - num2

# Test Cases

def test_calculator_cache():
    c = Calculator()
    assert hasattr(c, 'cache')
    assert c.cache == {}

    assert c.add(2, 8) == 10
    assert c.cache == {
        'add': [
            (2, 8, 10)
        ]
    }

    assert c.subtract(7, 2) == 5
    assert c.cache == {
        'add': [
            (2, 8, 10)
        ],
        'subtract': [
            (7, 2, 5)
        ]
    }

    assert c.subtract(11, 7) == 4
    assert c.cache == {
        'add': [
            (2, 8, 10)
        ],
        'subtract': [
            (7, 2, 5),
            (11, 7, 4)
        ]
    }

    # Repeated operation. Should be cached
    assert c.add(2, 8) == 10
    assert c.cache == {
        'add': [
            (2, 8, 10)
        ],
        'subtract': [
            (7, 2, 5),
            (11, 7, 4)
        ]
    }