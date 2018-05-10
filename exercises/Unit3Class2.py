#Unit3/Advanced Functions/Class2

'''
1) Know Scope

Analyze the following code and answer:
What will be the final value of c after the execution of this code:

a = 10
b = 3
c = 7
def test_scope(b):
    a = 11
    return a + b + c

c = c + test_scope(5)

whats_the_value_of_c = ?
'''

whats_the_value_of_c = 30

# Test Cases 

def test_scope():
    assert whats_the_value_of_c == 30



'''
2) Calculate Annual Income

Write a function calculate_annual_income with two parameters: hourly_rate and hours_per_week. You could design hours_per_week to be a required parameter, but for this assignment, since many people work 40 hours per week, you're going to 
design it as a default/optional argument set to 40.

There are 52 weeks in a year, so all we need to do is multiply the hourly_rate by hours_per_week and multiply that by 52.

calculate_annual_income(15.00)  # 31200.00
calculate_annual_income(12.00, hours_per_week=20) # 12480.00
'''

def calculate_annual_income(hourly_rate, hours_per_week=40):
    return hourly_rate * hours_per_week * 52

# Test Cases

def test_annual_income_default_hours():
    assert calculate_annual_income(12.00, hours_per_week=20)  == 12480.00

#

def test_annual_income_base():
    assert calculate_annual_income(15.00)  == 31200.00



'''
3) Add book to purchase

Write a function add_book_to_purchase that receives a dictionary with purchase information and adds a book to the given purchase dict. Each purchase dict has a key books that contains a list of books. Your job is to append the book to that 
list.
'''

def add_book_to_purchase(purchase_dict, title, author, price=0.99):
    purchase_dict['books'].append({
        'title': title, 
        'author': author, 
        'price': price
    })
    return purchase_dict

# Test Cases 

def test_add_book_to_purchase_base_use_case():
    purchase = {
        'id': 99,
        'books': [{
            'title': 'The Raven',
            'author': 'Edgar Allan Poe',
            'price': 19.99
        }, {
            'title': 'Ulysses',
            'author': 'James Joyce',
            'price': 23.99
        }],
        'total': 0
    }

    add_book_to_purchase(
        purchase,
        title='The Odyssey',
        author='Homer',
        price=7.99)

    assert len(purchase['books']) == 3
    assert purchase['books'] == [{
        'title': 'The Raven',
        'author': 'Edgar Allan Poe',
        'price': 19.99
    }, {
        'title': 'Ulysses',
        'author': 'James Joyce',
        'price': 23.99
    }, {
        'title': 'The Odyssey',
        'author': 'Homer',
        'price': 7.99
    }]

#

def test_add_book_to_purchase_default_price():
    purchase = {
        'id': 99,
        'books': [{
            'title': 'The Raven',
            'author': 'Edgar Allan Poe',
            'price': 19.99
        }, {
            'title': 'Ulysses',
            'author': 'James Joyce',
            'price': 23.99
        }],
        'total': 0
    }

    add_book_to_purchase(
        purchase,
        title='The Odyssey',
        author='Homer')

    assert len(purchase['books']) == 3
    assert purchase['books'] == [{
        'title': 'The Raven',
        'author': 'Edgar Allan Poe',
        'price': 19.99
    }, {
        'title': 'Ulysses',
        'author': 'James Joyce',
        'price': 23.99
    }, {
        'title': 'The Odyssey',
        'author': 'Homer',
        'price': 0.99
    }]



'''
4) Calculate purchase price
Base case

Following the same structure from the previous assignment, define a function calculate_purchase_price that receives a purchase dictionary and computes the sum of the prices of all the books contained in that purchase. The function, by default, should NOT update the value in the purchase dict.

Example:

purchase = {
    'id': 99,
    'books': [{
        'title': 'Book A',
        'author': 'Author A',
        'price': 3
    }, {
        'title': 'Book B',
        'author': 'Author B',
        'price': 5
    }],  # Empty list of books
    'total': 0
}

total = calculate_purchase_price(purchase)
print(total)  # 8
print(purchase['total'])  # 0  # Not updated. IMPORTANT #
'''

def calculate_purchase_price(purchase, set_to_dict=False):
    total = 0
    books = purchase['books']
    for book in books:
        total += book['price']
    if set_to_dict:
        purchase['total'] = total
    return total   

# Test Cases 

def test_calculate_purchase_price_without_setting_dict():
    purchase = {
        'id': 99,
        'books': [{
            'title': 'The Raven',
            'author': 'Edgar Allan Poe',
            'price': 19.99
        }, {
            'title': 'Ulysses',
            'author': 'James Joyce',
            'price': 23.99
        }, {
            'title': 'The Odyssey',
            'author': 'Homer',
            'price': 7.99
        }],
        'total': 0
    }
    total = calculate_purchase_price(purchase)
    assert total == 51.97
    assert purchase['total'] == 0

#

def test_calculate_purchase_price_setting_to_dict():
    purchase = {
        'id': 99,
        'books': [{
            'title': 'The Raven',
            'author': 'Edgar Allan Poe',
            'price': 19.99
        }, {
            'title': 'Ulysses',
            'author': 'James Joyce',
            'price': 23.99
        }, {
            'title': 'The Odyssey',
            'author': 'Homer',
            'price': 7.99
        }],
        'total': 0
    }
    total = calculate_purchase_price(purchase, set_to_dict=True)
    assert total == 51.97
    assert purchase['total'] == 51.97



'''
5) Multi-search

Write a function search_animals that receives 3 parameters:
a required parameter called list_of_animals that receives a list of animal dictionaries
an optional parameter called given_name that will be used as an optional search term
* an optional parameter called animal_type that will be used as an optional search term

First, take a good look at the structure of the example animal list.

animals = [
        {
            "animal_type": "Raccoon",
            "street_name": "Trash Panda",
            "given_name":  "Gizmo"
        },
        {
            "animal_type": "Snake",
            "street_name": "Danger Noodle",
            "given_name":  "Spaghetti"
        },
        {
            "animal_type": "Snake",
            "street_name": "Danger Noodle",
            "given_name":  "Nope"
        },
        {
            "animal_type": "Penguin",
            "street_name": "Formal Chicken",
            "given_name":  "Mclovin"
        },
        {
            "animal_type": "Sting ray",
            "street_name": "Sea Pancake",
            "given_name":  "Flap Flap"
        },
        {
            "animal_type": "Guinea Pig",
            "street_name": "Furry Potato",
            "given_name":  "Alf"
        },
        {
            "animal_type": "Platypus",
            "street_name": "Duck Puppy",
            "given_name":  "Bill"
        },
        {
            "animal_type": "Seagull",
            "street_name": "Beach Chicken",
            "given_name":  "Santiago"
        },
        {
            "animal_type": "Ferret",
            "street_name": "Cat Snake",
            "given_name":  "Will Ferret"
        }
]

The goal is to be able to search this list of animals by the animal's given_name and/or the animal_type, for each of those combinations.

Optional arguments enable you to have these types of search combinations.

If they enter a given_name search term, you'll want to check all the animals in the list and see if the search term is in their value associated with the key given_name.

There could be multiple matches, so we want to store our matching animal dictionaries in a list.

Do the same thing for animal_type search term, but for that check if the search term is in either the value associated with the key animal_type OR street_name. Hope you remembered your operators lessons :)

Your default values here should be set to None by default so it is easy to check what kind of search the user is doing based on which of the optional arguments aren't None.
'''

def search_animals(list_of_animals, given_name = None, animal_type = None):
    matching_animals = []
    for animal in animals:
        if given_name:  
            if animal['given_name'] == given_name:
                matching_animals.append(animal)
        elif animal_type:
            if (animal_type in animal['animal_type']) or (animal_type in animal['street_name']):
                matching_animals.append(animal)
    if given_name == None and animal_type == None:
        return list_of_animals
    return matching_animals

# Test Cases

expected_animal_types = [{
    'animal_type': 'Penguin',
    'given_name': 'Mclovin',
    'street_name': 'Formal Chicken'
}, {
    'animal_type': 'Seagull',
    'given_name': 'Santiago',
    'street_name': 'Beach Chicken'}
]

def test_search_animal_type():
    assert search_animals(animals, animal_type="Chicken") == expected_animal_types

#

expected_given = [{
    "animal_type": "Ferret",
    "street_name": "Cat Snake",
    "given_name": "Will Ferret"
}]

def test_search_given_name():
    assert search_animals(animals, given_name="Will Ferret") == expected_given

#

expected = [{
    "animal_type": "Snake",
    "street_name": "Danger Noodle",
    "given_name": "Nope"
}]

def test_search_given_and_animal_type():
    assert search_animals(animals, animal_type="Snake", given_name="Nope") == expected

#

def test_no_search_terms():
    assert search_animals(animals) == animals

