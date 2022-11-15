string=input("enter a string: ");

substr=input("enter a substring: ");


i=0;
j=0;

while i<len(string):
    if string[i]==substr[j]:
        j+=1;
        pass;
    else:
        j=0;
        pass;
    i+=1;

    if j==len(substr):
        break;

    pass;

if j==len(substr):
    print(f"{substr} is in {string}\n");
    pass;
else:
    print(f"{substr} is not in {string}\n");
    pass;
