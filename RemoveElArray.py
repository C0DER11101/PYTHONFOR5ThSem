import array as arr

a=arr.array('i', [1, 2, 3, 4, 5, 6]);

print("Initial array: ", a);
#index=int(input("enter index of element to be deleted: "));
element=int(input("enter an element: "));

a.remove(element);

print("\nResultant array: ", a);

a.extend([element]);

print("\nResultant array: ", a);
