class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method.")

class Fish(Animal):
    def move(self):
        print("The fish swims gacelully through the waves. 🐠")

class Dog(Animal):
    def move(self):
        print("The Dog runs through the garden. 🐕")

class Bird(Animal):
    def move(self):
        print("The birds soars high in the sky. 🐦")

def animals_movement(animals):
    for animal in animals:
        animal.move()

# Instance tof each animal class
my_fish = Fish()
my_dog = Dog()
my_bird = Bird()

# 
zoo = [my_fish, my_dog, my_bird]

# CAll the animals_movement function

animals_movement(zoo)