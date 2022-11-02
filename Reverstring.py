String=input("enter a string: ");

print("\nInitial string:\n");
print(String);

print("\nReversed string:\n");

index=len(String);

for index in range(len(String)-1, -1, -1):
    print(String[index], end='');
print()
