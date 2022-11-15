# Simple matrix sum!!

matrix1=list();
matrix2=list();

row=int(input("enter number of rows: "));
col=int(input("enter number of columns: "));

el1=1;
el2=2;

for i in range(row):
    item1=list();
    item2=list();
    for j in range(col):
        item1.append(el1);
        item2.append(el2);
        el1+=1;
        el2+=1;
        pass;
    matrix1.append(item1);
    matrix2.append(item2)
    del item1;
    del item2;
    pass;


print("\nMatrix-1:\n");
for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end=' ');
        pass;
    print();
    pass;

print("\nMatrix-2:\n");
for i in range(row):
    for j in range(col):
        print(matrix2[i][j], end=' ');
        pass;
    print();
    pass;

print("\nSum:\n");
for i in range(row):
    for j in range(col):
        print(matrix1[i][j]+matrix2[i][j], end=' ');
        pass;
    print();
    pass;
