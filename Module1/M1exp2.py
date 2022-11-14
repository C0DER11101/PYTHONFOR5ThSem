"""
Name: Priyanuj Bora
Roll number: CSE-28/20

Experiment-2: Write a program in PYTHON to perform addition, subtraction, multiplication and division.
"""

# Addition of two numbers:
n1=int(input("enter first number: "));
n2=int(input("enter second number: "));

print(f"{n1} + {n2} = {n1+n2}\n");


# Subtraction of two numbers:
n1=int(input("enter first number: "));
n2=int(input("enter second number: "));

if n1>=n2:
    print(f"{n1} - {n2} = {n1-n2}\n");
    pass;
elif n2>n1:
    print(f"{n2} - {n1} = {n2-n1}\n");
    pass;


# Multiplication of two numbers:
n1=int(input("enter first number: "));
n2=int(input("enter second number: "));

print(f"{n1} x {n2} = {n2*n1}\n");

# Division of two numbers:
n1=int(input("enter first number: "));
n2=int(input("enter second number: "));

print(f"{n1} / {n2} = {n1/n2}\n");
