# Remove element from a list - the Python way

a=list();

size=int(input("enter size of the list: "));

for i in range(size):
    el=int(input(":"));
    a.append(el);
# end of for

print("Initial list: ", a);

element=int(input("enter element to be removed: "));

a.remove(element);

print("\nThe resultant array is: ", a);

num=int(input("how many elements do you want to insert into the list?: "));


for i in range(num):
    el=int(input(":"));
    a.append(el);
print("\nThe resultant array is: ", a);
