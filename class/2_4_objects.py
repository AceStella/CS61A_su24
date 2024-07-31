class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an object (instance) of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing class attribute
print(my_dog.species)  # Output: Canis familiaris

# Accessing instance attributes
print(my_dog.name)     # Output: Buddy
print(my_dog.age)      # Output: 3

# Using methods that interact with attributes
print(my_dog.description())  # Output: Buddy is 3 years old
print(my_dog.speak("Woof"))  # Output: Buddy says Woof