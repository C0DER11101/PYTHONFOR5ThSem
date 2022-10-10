def sort(a, size):
    for i in range(size):
        for j in range(size-1):
            if a[j]>a[j+1]:
                a[j], a[j+1]=a[j+1], a[j];
    return;

def binarySearch(a, size, element):
    beg=0; last=size-1; mid=0;
    i=0;

    while(i<size):
        mid=int((beg+last)/2);
        if a[mid]==element:
            print(f"{element} is in the array\n");
            return;
        elif a[mid]>element:
            last=mid-1;
        elif a[mid]<element:
            beg=mid+1;
        i+=1;
    return;


array=list();
size=int(input("enter size of the array: "));

for i in range(size):
    el=int(input("enter element: "));
    array.append(el);

sort(array, size);

print("Sorted array is:\n", array);

element=int(input("enter element to be searched: "));

binarySearch(array, size, element);
