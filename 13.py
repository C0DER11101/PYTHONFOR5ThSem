#Write a program in PYTHON to calculate the sum of the first 10 numbers. Also write the
#algorithm and calculate the worst case complexity and space complexity.

import time
s=time.time(); # starting time of program

num=int(input("enter num: "));
sumN=0;
for i in range(1, num+1):
    sumN+=i;
    
print(sumN);

e=time.time();  # ending time of program

# worst case: if num is large

print(e-s);