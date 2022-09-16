# Write a program in Python to find the maximum and minimum number in a array. Also write the algorithm.a=list();

size=int(input("enter size of the array: "));


for i in range(size):
    el=int(input(": "));
    a.append(el);

max=0;
min=a[len(a)-1];

for i in range(size):
    if a[i]>max:
        max=a[i];

    if a[i]<min:
        min=a[i];

print(f"Maximum element: {max}\n");
print(f"Minimum element: {min}\n");
