# for, while, break and continue in python

num=int(input("enter a number: "));

for i in range(num):
    print(i, end=" ");

    if i == num-4:
        print("Good bye!!\n");
        break;

i=0;

while i<10:
    print(i, end=" ");

    i+=1;

print();


while True:
    a=int(input("enter a number: "));

    if a%2==0:
        continue; # same C/C++ continue statement

    else:
        break; # same as C/C++ break statement
