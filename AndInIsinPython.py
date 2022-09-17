# and, or, not, is and in keywords in python.....

print(False or True);

print(True and False);

print(not True);
print(not False);


if 'nd' in 'apprehend': # in checks membership of an identifier in a particular array(array of characters i.e strings, or numbers).
    print("substring exists!!\n\n");

else:
    print("substring doesnot exist!!\n");


for i in 'Priyanuj':
    print(i, end=" ");  # i iterates through the string 'Priyanuj' and displays each character!!

print("\r"); # \r is carriage return in python(and in C/C++)


print(' ' is ' ');

print({} is {});

a=10;
b=10;

print(id(a));
print(id(b));

print(a is b);

# is basically returns true if both the variables have the same address, here a and b point to the same memory location
# of the integer value 10, hence they have the same location address, so a is b returns True.
