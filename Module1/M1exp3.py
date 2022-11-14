"""
Name: Priyanuj Bora
Roll number: CSE-28/20

Experiment-3: Write a program in PYTHON to find the maximum and minimum number in an array.
"""

import array as arr

a=arr.array('i', []); # empty array!!
size=int(input("enter size of the array: "));

for i in range(size):
    el=int(input(": "));
    a.append(el);
    pass;



print("\nHere is your array:\n");
for i in range(size):
    print(a[i], end=' ');
    pass;

maxNum=-1;
minNum=max(a);

for i in range(size):
    if a[i]>maxNum:
        maxNum=a[i];
        pass;
    if a[i]<minNum:
        minNum=a[i];
        pass;

    pass;

print(f"\nMaximum number in the array is {maxNum}");
print(f"\nMinimum number in the array is {minNum}");
print();
