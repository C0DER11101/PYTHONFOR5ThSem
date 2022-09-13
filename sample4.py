a=[]
b=[]

for i in range(5):
    el=int(input(":"));
    a.append(el);
    
b.append(a);

print(a);
print(b);
b.append(a);
print(b);
print(b[0][0])