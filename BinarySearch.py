import time

# time complexity: O(logn) -> log to the base 2
# space complexity: O(1)

arr=list();

size=int(input("enter size of the array: "));

for i in range(size):
    el=int(input(f"element {i+1}: "));
    arr.append(el);

element=int(input("enter element to be searched: "));

low=0;
high=len(arr)-1;

s=time.time();
while low<=high:
    mid=int((low+high)/2); # typcasting the result into integer!!

    if arr[mid]==element:
        print(f"{element} found at index {mid}!!\n\n");
        break;
    elif arr[mid]<element:
        low=mid+1;

    else:
        high=mid-1;

e=time.time();
print(e-s);