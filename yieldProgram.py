# Implementing yield!

def func():
	print("Inside func()\n");

	for i in range(10):
		print(f"Yield {i}", end=' ');
		yield i;


for i in func():
	print(i);
print("Here is a print()");
