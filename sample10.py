# test program:

arr=list();

size=int(input("enter size of the array: "));

print("enter elements into the array: ");

for i in range(size):
	el=int(input(":"));
	arr.append(el);

mid=len(arr)//2;

print(f"Array: {arr}");
print(f"Mid = {mid}");
print(arr[:mid]);
print(arr[mid:]);

print(len(arr[:mid]));
print(len(arr[mid:]));
