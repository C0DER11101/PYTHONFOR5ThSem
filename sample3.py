a=[]

print("\nenter elements into list a:\n");
a.append([int(j) for j in input().split()])

print("\nenter elements into list b:\n");
b=[int(j) for j in input().split()];

print("\nenter elements into list c:\n");
c=input().split();

print("\nenter elements into list d:\n");
d=[str(j) for j in input().split()];


print("\nlist-d:\n");
print(d);

print("\nlist-c:\n");
print(c);

print("\nlist-b:\n");
print(b);

print("\nlist-a:\n");
print(a);
