"""
Name: Priyanuj Bora
Roll number: CSE-28/20

Experiment-5: Write a program in PYTHON to check whether a certain phrase or character is present in a string or not.
"""

string=input("enter a string: ");
substr=input("enter a substring: ");

if substr in string:
    print(f"{substr} is in {string}!!\n");
    pass;
else:
    print(f"{substr} is not in {string}!!\n");
    pass;
