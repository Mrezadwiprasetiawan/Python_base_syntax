# Import dari modul lain
import module1
from module2 import another_function, function_from_module2

def main():
    # Memanggil fungsi dari module1
    print("Calling functions from module1:")
    module1.function1()
    module1.use_function_from_module2()

    # Memanggil fungsi dari module2
    print("\nCalling functions from module2:")
    function_from_module2()
    another_function()

    # List comprehension
    print("\nList comprehension example:")
    squares = [x**2 for x in range(10)]
    print(squares)

    # Lambda function
    print("\nLambda function example:")
    add = lambda a, b: a + b
    print(f"Sum of 5 and 3 is {add(5, 3)}")

    # Exception handling
    print("\nException handling example:")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Exception handling completed")

    # Class and object example
    print("\nClass and object example:")
    person = Person("Alice", 30)
    person.introduce()

    # Decorators example
    print("\nUsing decorators:")
    say_hello_decorated()

    # Generators example
    print("\nGenerators example:")
    for num in count_up_to(5):
        print(num)

    # Context Manager example
    print("\nContext Manager example:")
    with MyContextManager() as cm:
        print("Inside context")

if __name__ == "__main__":
    main()

# Class definitions and functions

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

# Decorator definition
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello_decorated():
    print("Hello!")

# Generator function
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Context Manager class
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
