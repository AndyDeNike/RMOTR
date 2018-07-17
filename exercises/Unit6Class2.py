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

'''        