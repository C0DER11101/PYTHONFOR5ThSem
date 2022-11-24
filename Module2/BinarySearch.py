# Binary search using python.

import array as arr

def sort(ar, size):
    for i in range(size):
        for j in range(size-1):
            if ar[j]>ar[j+1]:
                ar[j], ar[j+1]=ar[j+1], ar[j];
                pass;
            pass;
        pass;
    return;

def BinS(ar, size, element):
    last=size-1;
    beg=0;

    while beg<=last:
        mid=int((beg+last)/2);
        if ar[mid]==element:
            return 0;
        elif ar[mid]>element:
            larst=mid-1;
        elif ar[mid]<element:
            beg=mid+1;
    return -1;

size=int(input("enter the size of the array: "));

ar=arr.array('i',);

print("enter elements into the array:\n");

for i in range(size):
    el=int(input(":"));
    ar.append(el);
    pass;


print("This is your original array:\n");

for i in range(size):
    print(ar[i], end=' ');
    pass;
print();

sort(ar, size);

print("This is your sorted array:\n");

for i in range(size):
    print(ar[i], end=' ');
    pass;
print();

element=int(input("enter element to be searched: "));

print("\nPerforming Binary Search\n");

if BinS(ar, size, element)==0:
    print(f"{element} found in the array!!\n");
    pass;

else:
    print(f"{element} not found in the array!!\n\n");
    pass;
