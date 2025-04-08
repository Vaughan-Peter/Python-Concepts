# Base class
class Animal:
    def speak(self):
        pass

# Derived class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Derived class 3
class Cow(Animal):
    def speak(self):
        return "Moo!"

# Function that demonstrates polymorphism
def animal_sound(animal):
    print(animal.speak())

# Create instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Call the same function on different objects
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(cow)  # Output: Moo!