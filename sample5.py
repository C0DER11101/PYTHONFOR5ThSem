a=list();

print("enter size of the array: ");
size=int(input(":"));

print("enter elements into the array:\n\n");
for i in range(size):
    el=int(input(">"));
    a.append(el);
    
print("this is your array:\n", a);

# perform bubble sort
    
for i in range(size):
    for j in range(size-1):
        if a[j]>a[j+1]:
            temp=a[j];
            a[j]=a[j+1];
            a[j+1]=temp;
            

print(f"the sorted array is \n{a}\n");