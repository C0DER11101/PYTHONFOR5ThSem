# TO FIND THE MAXIMUM AND MINIMUM NUMBER OF AN ARRAY

import array as arr

numbers=arr.array('i',[1, 2, 7, 9, 11])

maxm = numbers[0]

n=len(numbers)

# finding maximum element
for i in range(0, n):
    if(numbers[i]>maxm):
        maxm=numbers[i];
        
print(f"Largest element {maxm}")

minm=numbers[4]

# finding minimum element
for i in range(0, n):
    if(numbers[i]<minm):
        minm=numbers[i]
        

print(f"Smallest element {minm}")