"""
Name: Priyanuj Bora
Roll number: CSE-28/20

Experiment-7: Write a program in PYTHON to calculate the sum of the first 10 numbers. Also write the algorithm and calculate the worst case complexity and space complexity.
"""

import time

print("\nSum of the first 10 numbers is:", end=' ');

s=time.time();
Sum=0;
for i in range(1, 11):
    Sum+=i;
    pass;

print(f"{Sum}\n");

e=time.time();

print(f"Time = {e-s}\n");
