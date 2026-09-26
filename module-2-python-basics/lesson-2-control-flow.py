"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Ethan Miguel P. Patio
Date: September 26, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[This topic is about the control flow, decision making, and conditions using if/elif/else. First, I made some variables named "age" and "name", I want to check if I can already vote, so I made a simple code to see if I can vote or not. The translation of my code is "if my age is above 18, I can vote already, same as the elif statement. But is my age is below 18, I cannot vote."]


============================================
KEY VOCABULARY
============================================
- condition: it continues if the condition is true, and blocks the code if the condition is false
- if / elif / else: "if" is the initial check, "elif" is the backup, and "else" is the final catch
- comparison operator: symbols that are used to compare 2 or more values
- boolean expression: checks any line of code if the expression is true or false
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

age = 21
name = "Ethan"

if age > 18:
    print(f"{name} is 18 above! he can already vote!")
elif age == 18:
    print(f"{name} is exactly 18! he can vote!")
else:
    print(f"{name} cannot vote...")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[The mistake I made that I want to avoid is incorrectly indenting the "else" statement]

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
