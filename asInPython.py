# The as keyword in Python

# this keyword is used to create an alias for the module imported.

import math as meh

num=int(input("enter a number: "));

print(f"\nThe factorial of {num} is: ", end=' ');
print(meh.factorial(num));
