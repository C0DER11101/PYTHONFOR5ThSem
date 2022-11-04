# File I/O in Python

f=open("hello.txt", "a");

f.write("Later aligator!!");

f.close();

f=open("hello.txt");

content=f.read();

print(content);

f.close();

f=open("hello1.txt", "w");

f.write("This is a text file!\n");
f.close();


f=open("hello1.txt");
content=f.read();

f.close();

print(content);
