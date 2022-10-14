# test

for i in range(1, 5):  # prints all numbers from 1 to 4 (5 is excluded)
	print(i, end=' ');

print();


a=list();

size=int(input("enter size of the array: "));

for i in range(size+1):
	a.append(0);

print(a);

for i in range(1, size+1):
	print("enter element ", i);
	a[i]=int(input(":"));

print(a);

for i in range(1, size+1):
	print(a[i], end=' ');

print();
