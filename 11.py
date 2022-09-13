# Write a program in python to check whether a certain phrase or character is present
# in the string or not

# initializing string
test_str="Priyanuj"

# using str.find() to test
# for substring
res = test_str.find("Priyanuj");
if res >= 0:
    print("String is present in the string!!\n\n");
    
else:
    print("string is not present in the string!!\n\n");