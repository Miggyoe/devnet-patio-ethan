"""
Module 2 — Lesson 4: functions
Student: Ethan Miguel P. Patio
Date: September 26, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[This topic is about functions. Function is a block of code that can be reuse multiple times, instead of writing a block of code many times, use function. Parameters are like a placeholder that are waiting to be filled with value. Return values are the output that a function sends back. In my example, I made a function called "greetings", instead of writing the code multiple times just to greeting each person, I used the function and just called it with the values. Since the parameters are "name, age", I matched it with "Ethan" and a number. To show how the return works, I used a math operations. For example, the function "add" has a parameter of x and y, those two parameter will be added and will be contained inside the "sum" variable. Since the operation is done, I want to get the output "sum" by just typing "return sum". By printing the function and putting a whole number inside the parameter "print(add(5,5))", the output that has been sent back by the function is 10. That's how the function works


============================================
KEY VOCABULARY
============================================
- function: block of reusable code
- parameters: placeholder inside the "()" of a function
- return values: output that a function sends back
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def greetings(name, age):
    print(f"Hello {name}!")
    print(f"You are {age} years old!")
    print()

greetings("Ethan", 20)
greetings("Gabriel", 16)
greetings("Samuel", 9)

print("="*20)

def add(x, y):
    sum = x + y
    return sum
def sub(x, y):
    dif = x - y
    return dif
def mul(x, y):
    pro = x * y
    return pro
def div(x, y):
    quo = x / y
    return quo

print(add(5, 5))
print(sub(5, 5))
print(mul(5, 5))
print(div(5, 5))

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[The mistake I made that I want to avoid is put a double quotation marks inside the parameters of a function]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
