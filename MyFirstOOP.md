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
