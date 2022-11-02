# Multiply two matrices!!

print("\nMATRIX-1\n");
matrix1=list();
row1=int(input("enter number of rows: "));
col1=int(input("enter number of columns: "));

print("\nMATRIX-2\n");
matrix2=list();
row2=int(input("enter number of rows: "));
col2=int(input("enter number of columns: "));

if col1!=row2:
    print("\nCannot multiply matrices!!\n");

elif col1==row2:
    print("\nMATRIX-1\n");
    print("\nenter elements:\n");

    for i in range(row1):
        matrix1.append([int(j) for j in input().split()]);
#end

    print("\nMATRIX-2\n");
    print("\nenter elements:\n");

    for i in range(row2):
        matrix2.append([int(j) for j in input().split()]);
#end
    print("\nMatrix-1:\n");
    for i in range(row1):
        for j in range(col1):
            print(matrix1[i][j], end=' ');
        print();

    print("\nMatrix-2:\n");
    for i in range(row2):
        for j in range(col2):
            print(matrix2[i][j], end=' ');
        print();

    sum=0;

    print();
    print("\nResultant matrix:\n");

    for i in range(row1):
        for j in range(col2):
            sum=0;
            for k in range(col1):
                sum+=matrix1[i][k]*matrix2[k][j];
            print(sum, end=' ');
        print();
