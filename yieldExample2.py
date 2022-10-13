# Example

def func():

	yield "Hello world";
	yield "Priyanuj Bora";

obj=func();

"""for i in obj:
	print(i);
	"""

print("Using next():");
print(type(obj));
print(next(obj));
print(next(obj));
