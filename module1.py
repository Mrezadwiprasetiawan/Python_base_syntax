def function1():
    print("This is function1 from module1")

def function2():
    print("This is function2 from module1")

# Import dari module2
from module2 import function_from_module2

def use_function_from_module2():
    function_from_module2()
