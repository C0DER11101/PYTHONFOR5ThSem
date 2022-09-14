# range() FUNCTION IN PYTHON

for step in range(5): # start from 0 and go till 5-1 i.e. 4
    print("Step ", step);
    
print("-------------------------");

for step in range(0, 13, 2):
    print("Step ", step);
    
print("-------------------------");

num_Steps=int(input("enter number of steps: "));

for step in range(0, num_Steps, 2):# if num_Steps is odd then it will iterate num_Steps-1
    print("Step ", step);
# if num_Steps is even, then it will iterate till num_Steps-2