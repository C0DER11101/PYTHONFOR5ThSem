#Write a program in PYTHON to sum the series 1/2 + 2/3 +..........+n/n+1.
#Also write the algorithm and calculate 
#the worst case complexity and space complexity.

import time
num=int(input("enter num: "));

s=time.time();

suM=float();

for n in range(1, num+1):
    suM+=n/(n+1);
    

e=time.time();

print(f"Sum is {suM}\n\n");
print(e-s);