# Assignment 1
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


circle = Circle(3)
print(circle.area())
rectangle = Rectangle(3, 2)
print(rectangle.area())

# Assignment 2


class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}'s Account: Balance of {self.balance}"

    def __add__(self, other):
        return self.balance + other.balance


fred = BankAccount(500, "Fred")
ethel = BankAccount(600, "Ethel")
print(fred)
print(ethel)
print(fred + ethel)
