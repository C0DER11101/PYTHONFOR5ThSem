# MODULES IN PYTHON

import math

def FindABS(num):  # arguments
    absInt=math.fabs(num);
    
    return absInt;

if __name__=="__main__":
    
    num=int(input("enter a number: "));
    print(f"Absolute value of a {num} is {int(FindABS(num))}\n");