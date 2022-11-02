# Remove element from an array

import array as arr

a=arr.array('i', [1, 2, 3, 4, 5, 6]);

print("\nInitial array: ", a);

element=int(input("enter element to be removed from the array: "));

a.remove(element);

print("\nResultant array: ", a);

elements=list();

print("how many elements do you want to insert into the array?: ");

num=int(input(">"));

for i in range(num):
    el=int(input(":"));
    elements.append(el);

a.extend(elements);
print("\nResultant array: ", a);
