"""
Name: Priyanuj Bora
Roll number: CSE-28/20

Experiment-6: Write a program in PYTHON to find the greatest of three numbers. Also write the algorithm and calculate the worst case complexity and space complexity.
"""

import time

a=int(input("enter first number: "));
b=int(input("enter second number: "));
c=int(input("enter third number: "));

s=time.time();
if a>b:
    if a>c:
        print(f"Largest: {a}\n");
        pass;
    else:
        print(f"Largest: {c}\n");
        pass;
    pass;

elif b>a:
    if b>c:
        print(f"Largest: {b}\n");
        pass;
    else:
        print(f"Largest: {c}\n");
        pass;
    pass;
e=time.time();

print(f"Time = {e-s}\n");
