str1=input("enter a string: ");
str2=input("enter a substring: ");

if str2 in str1:
    print(f"{str2} is in {str1}\n\n");
    
else:
    print(f"{str2} is not in {str1}\n\n");