arr=list();

size=int(input("enter size of the array: "));

print("enter elements into the array:\n\n");

for i in range(size):
	el=int(input(": "));
	arr.append(el);

print("length of the array is: ", len(arr));

print("Mid : ", len(arr)//2);  # // means floor division!!

mid=len(arr)//2;
print(arr[:mid]); # display elements till index mid-1!!
