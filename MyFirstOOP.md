## Comperhension check
1. **Class** is blueprint or a template for how something should be defined, but deos not provide any real content by itself
1. **Instance** is a copy of the class with actual values
1. Class is like form, it defines needed information. When you fill out the form, your specific copy is an instance of a class - it contains actual information
1. Python syntax used for defining a new class is CamelCase notation
```.py
class Animals:
    pass
```
5. Spelling convention for a class nameis
6. You create an instance by using name of the class and atrubutes you want to assign to it using syntax:
```.py
a = Dogs('pepe', 1)
b = Dogs('tesla', 3)
c = Dogs('MrP', 5)
```
7. Method is function defined inside class to perform operations with the atribures
8. Purpose of self is always the first argument
9.  We use ``` __init__``` to initialize and object's initial atributes by giving them their default value
10. With inheritance we can use class that is already created and just add to it
11.Child classes never override properties of their parrents, they can jsut add to it

## My first OOP practise
```.py
# Example bellow shows how to define a class with instances


# Parent class
class Dogs:
    # Class attribute, this will be the same for all objects
    species = 'mammal'

    # This are instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method (function)
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # Instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # Instance method
    def birthday(self):
        self.age += 1

class Pets:
    

# Child class (inherits from Dog class)
class RussellTerrier(Dogs):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


def get_biggest_number(*args):
    biggest = max(args)
    print(f'The oldest dog is {biggest} years old')


# Child class inherit atributes and behaviros from the parrent class
jim = RussellTerrier("Jim", 12)
print(jim.description())
# Child classes also have specific atributes
print(jim.run("slow"))


a = Dogs('pepe', 1)
b = Dogs('tesla', 3)
c = Dogs('MrP', 5)
get_biggest_number(a.age, b.age, c.age)

# call instance methods
print(a.description())
print(a.speak("Gruff Gruff"))
print(c.birthday())
´´´
