"""
Module 2 — Lesson 3: Loops & Lists
Student: Ethan Miguel P. Patio
Date: September 26, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[This topic is about loops and lists. List is a ordered collection of values (duplicates are okay). for loop iterates a block of code a specific number of times. In my example, for every fruit inside my fruits list, I print each fruit of it. Indexing is the numberical position inside the list. In my example, I printed out the "fruit[2]", since the starting number is 0, the coconut is printed. Lastly, the while loop repeats a block of codes as long as the condition is true. In my example, as long as "i" or index is less than the length of the fruits list, it will print the index starting from 0 (apple) and stop if the condition reaches 4 (orange).]


============================================
KEY VOCABULARY
============================================
- list: ordered collection, duplicates are OK
- for loop: repeats a block of code a specific number of times
- while loop: repeats a block of code as long the condition is true
- index: numerical position inside list (first is "0")
- iteration: repeating process of a loop
- len(): length or number of items inside a list
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

fruits = ["apple", "banana", "coconut", "pineapple", "orange"]
print("<forloop>")
for fruit in fruits:
    print(fruit)

print("="*10)

print("<indexing>")
print(fruits[2])

print("="*10)

print("<whileloop>")

i = 0

while i < len(fruits):
    print(fruits[i])
    i = i + 1

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[The mistake I made that I want to avoid is forgetting to declare the "i" (starting point which is 0)]

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
