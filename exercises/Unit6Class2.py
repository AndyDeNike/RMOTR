#Unit6/OOP Inheritance/Class2

'''
1) Friendly Animals

Extend the Animal class provided with three more subclasses: Cat, Dog, Human.

Include a method talk in each one of the subclasses. The talk method should return different options based on the type of animal:

    Cat: should return "Meow!"
    Dog: should return "Ruff!"
    Human: should return "Hello!"
'''

class Animal(object):
    pass

class Cat(Animal):
    def talk(self):
        return "Meow!"
        
class Dog(Animal):
    def talk(self):
        return "Ruff!"
        
class Human(Animal):
    def talk(self):
        return "Hello!"

# Test Cases

def test_animals_talking():
    cat = Cat()
    dog = Dog()
    human = Human()

    assert isinstance(cat, Animal)
    assert isinstance(dog, Animal)
    assert isinstance(human, Animal)

    assert cat.talk() == 'Meow!'
    assert dog.talk() == 'Ruff!'
    assert human.talk() == 'Hello!'



'''
2) Cow Says Moo

Extend the Animal class with three different subclasses: Cow, Sheep, and Fox.

When each animal is created, it should receive a name as a parameter. Rather than having a talk method in each subclass, you can just put one talk method in the parent Animal class and have the subclasses use that.

The talk method should say "[Animal_name] says [Animal_sound]"

Each subclass should have a sound attribute for that particular animal.

    The sound for Cow is "moo"
    The sound for Sheep is "baaaaa"
    The sound for Fox is "Ring-ding-ding-ding-dingeringeding"

Try and take advantage of the super keyword in the subclasses for the __init__ method (the Animal class should only store the attribute name, but the subclasses also store the attribute sound).

Example:

sheep = Sheep("Baaab")
print(sheep.sound) # baaaaa
print(sheep.talk()) # Baaab says baaaaa
'''

class Animal(object):
    def __init__(self, name):
        self.name = name 
    def talk(self):
        return "{} says {}".format(self.name, self.sound)

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "moo" 

class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "baaaaa"

class Fox(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Ring-ding-ding-ding-dingeringeding"

# Test Cases 

def test_animals():
    cow = Cow('Bessie')
    sheep = Sheep('Fuzzy')
    fox = Fox('Red')

    assert isinstance(cow, Animal)
    assert isinstance(sheep, Animal)
    assert isinstance(fox, Animal)

    assert cow.sound == "moo"
    assert sheep.sound == "baaaaa"
    assert fox.sound == "Ring-ding-ding-ding-dingeringeding"

    assert cow.talk() == "Bessie says moo"
    assert sheep.talk() == "Fuzzy says baaaaa"
    assert fox.talk() == "Red says Ring-ding-ding-ding-dingeringeding"



'''
3) Payroll

Create a class Employee with two subclasses: SalariedEmployee and HourlyEmployee.

Employee receives a name parameter and has a __str__ method (prints like "[name] makes [annual_income] annually").

SalariedEmployee should receive parameters for name and salary. It has a method calculate_annual_income that returns the salary for that person.

HourlyEmployee should receive parameters for name and hourly_wage. It has a method calculate_annual_income that returns the annual income, calculated by multiplying the hourly_wage * 40 (hrs per week) * 52 (weeks).

The Payroll class receives a parameter for company and an optional argument for employee_list. If there is no employee_list, set it to an empty list. It has two methods:
- add_employee receives an employee as a parameter and adds it to the employee_list
- get_annual_payroll_cost adds up the total annual income for each employee in the employee_list and returns it

Example:

emp1 = SalariedEmployee("Bill", 60000)
emp2 = HourlyEmployee("Ted", 25)

emp1.name # "Bill"
emp1.calculate_annual_income() # 60000
print(emp1) # "Bill makes 60000 annually"

emp1.calculate_annual_income() # 60000
emp2.calculate_annual_income() # 52000

payroll = Payroll("Excellent Adventures")
payroll.company # "Excellent Adventures"

payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.get_annual_payroll_cost() # 112000
'''        

class Payroll(object):
    def __init__(self, company, employee_list=None):
        self.company = company
        if not employee_list:
            employee_list = []
        self.employee_list = employee_list

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def get_annual_payroll_cost(self):
        total = 0
        for employee in self.employee_list:
            total += employee.calculate_annual_income()
        return total


class Employee(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{name} makes {income} annually".format(name=self.name, income=self.calculate_annual_income())


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super(SalariedEmployee, self).__init__(name)
        self.salary = salary

    def calculate_annual_income(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage):
        super(HourlyEmployee, self).__init__(name)
        self.hourly_wage = hourly_wage

    def calculate_annual_income(self):
        return self.hourly_wage * 40 * 52

#Test Cases

def test_salaried():
    emp1 = SalariedEmployee("Bill", 60000)

    assert emp1.name == "Bill"
    assert emp1.salary == 60000

    assert emp1.calculate_annual_income() == 60000
    assert str(emp1) == "Bill makes 60000 annually"

def test_payroll():
    emp1 = SalariedEmployee("Bill", 60000)
    emp2 = HourlyEmployee("Ted", 25)
    
    payroll = Payroll("Excellent Adventures")
    assert payroll.company == "Excellent Adventures"

    payroll.add_employee(emp1)
    payroll.add_employee(emp2)
    assert payroll.get_annual_payroll_cost() == 112000

def test_hourly():
    emp1 = HourlyEmployee("Ted", 25)

    assert emp1.name == "Ted"
    assert emp1.hourly_wage == 25

    assert emp1.calculate_annual_income() == 52000
    assert str(emp1) == "Ted makes 52000 annually"
