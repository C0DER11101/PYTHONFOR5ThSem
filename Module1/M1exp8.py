"""
Name: Priyanuj Bora
Roll number: CSE-28/20

Experiment-8: Write a program in PYTHON to sum the series 1/2 + 2/3 +..........+n/n+1. Also write the algorithm and calculate the worst case complexity and space complexity.
"""

import time

length=int(input("enter value of n: "));

s=time.time();

Sum=0;
for n in range(1, length+1):
    Sum+=n/(n+1);
    pass;

print(f"Sum is: {Sum}\n");

e=time.time();

print(f"Time = {e-s}\n");
