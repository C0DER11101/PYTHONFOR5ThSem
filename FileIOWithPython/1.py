#  File I/O in Python!!

f=open("hello.txt");

content=f.read();

f.close();
print(content);

f=open("hello.txt");

for line in f:
    print(line);
    pass

f.close();

f=open("hello.txt");
print(f.readlines());
f.close();
