import array as arr

def BinSearch(a, size, element):
    beg=0; last=size-1;
    while beg<=last:
        mid=int((beg+last)/2);

        if a[mid]==element:
            return True;
        elif a[mid]<element:
            beg=mid+1;
            pass;
        elif a[mid]>element:
            last=mid-1;
            pass;
        pass;
    return False;

a=arr.array('i');

size=int(input("enter size of the array: "));
print("enter elements in sorted order:\n");

for i in range(size):
    el=int(input(":"));
    a.append(el);
    pass;


print("\nHere is the array:\n");
for i in range(size):
    print(a[i], end=' ');
    pass;
print();

element=int(input("enter element to be searched for: "));

if BinSearch(a, size, element):
    print(f"{element} is in the array!!\n");
    pass;
else:
    print(f"{element} is not in the array!!\n");
    pass;
