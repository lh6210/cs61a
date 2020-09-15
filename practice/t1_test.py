
from math import sqrt

def fib_test():
    assert fib(2) == 1, 'the second Fib number should be 1'
    assert fib(3) == 1, 'the third fib number should be 1'
    assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'


class MyFirstClass:
    pass

class Point:
    "Represent point in x-y plane"

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def reset(self):
        self.x, self.y = 0, 0

    def move(self, x, y):
        self.x, self.y = x, y
        
    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
