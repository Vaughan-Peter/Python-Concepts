# Base class (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

    def description(self):
        return f"{self.name} is an animal."

# Derived class (Child class)
class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)  # Call the constructor of the parent class
        self.breed = breed
        self.age = age

    # Overriding the speak method
    def speak(self):
        return f"{self.name} barks loudly!"

    def description(self):
        return f"{self.name} is a {self.age}-year-old {self.breed} dog."

# Another derived class (Child class)
class Cat(Animal):
    def __init__(self, name, color, age):
        super().__init__(name)
        self.color = color
        self.age = age

    def speak(self):
        return f"{self.name} meows softly."

    def description(self):
        return f"{self.name} is a {self.age}-year-old {self.color} cat."

# Create objects of the derived classes
dog = Dog("Buddy", "Golden Retriever", 3)
cat = Cat("Whiskers", "Black", 5)

# Expanded print statements with more detailed information
print(f"Dog Info: {dog.description()}")
print(f"Dog's Sound: {dog.speak()}")
print()  # New line for separation
print(f"Cat Info: {cat.description()}")
print(f"Cat's Sound: {cat.speak()}")