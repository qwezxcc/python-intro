import pygame
import sys
# --------------------------------------
# клас велосипед

class Bike:
    name = ''
    gear = ''

    def go(self):
        print(self.name, ' - почав їхати')

bike1 = Bike()
bike2 = Bike()
bike3 = Bike()

bike1.name = 'Track'
bike1.gear = 'Helmet'

print(bike1.name, bike1.gear)
bike1.go()

print('-'*50)
# ----------------------------------------------
class Dog:
    name = None
    age = None
    breed = None

    def bark(self):
        print(f"{self.name}, гавкає")

    def run(self):
        print(f"{self.name}, біжить")

    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Порода: {self.breed}")


# creating dog

dog1 = Dog()
dog1.name = 'idk'
dog1.age = 3
dog1.breed = 'idk'
dog1.bark()
dog1.run()
dog1.info()

# creating dog 2
dog2 = Dog
