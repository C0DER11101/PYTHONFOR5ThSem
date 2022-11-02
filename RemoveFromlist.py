# To remove element from a list- The C/C++ way!!

def removeElement(a, size, element):

    for i in range(size):
        if a[i]==element:
            j=i
            while j<size-1:
                a[j]=a[j+1];
                j+=1;

    size-=1;
    return size;

a=list()

size=int(input("enter size of the array: "));
print("enter elements into the list: ");

for i in range(size):
    el=int(input(":"));
    a.append(el);


el=int(input("enter element to remove: "));

size=removeElement(a, size, el);

print("\nThe resultant list is:\n");

for i in range(size):
    print(a[i], end=' ');

print();
