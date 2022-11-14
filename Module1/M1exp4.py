"""
Name: Priyanuj Bora
Roll number: CSE-28/20

Experiment-4: Write a program in PYTHON to find the summation of 2d matrices.
"""

print("\nMATRIX-1\n");
mat1=list();  # matrix-1
row1=int(input("enter number of rows: "));
col1=int(input("enter number of columns: "));

print("\nMATRIX-2\n");
mat2=list();  # matrix-2
row2=int(input("enter number of rows: "));
col2=int(input("enter number of columns: "));


if row1==row2 and col1==col2:

    #------------------ Inserting elements into the matrices ------------------#

    # MATRIX-1
    print("\nMATRIX-1\n");

    for i in range(row1):
        mat1.append([int(j) for j in input().split()]);
        pass;

    print("\nMATRIX-2\n");
    for i in range(row2):
        mat2.append([int(j) for j in input().split()]);
        pass;

    Sum=list();

    for i in range(row1):
        sums=list();
        for j in range(col1):
            sums.append(mat1[i][j]+mat2[i][j]);
            pass;
        Sum.append(sums);
        del sums;
        pass;

    print("\nThe resultant matrix is:\n");

    for i in range(row1):
        for j in range(col1):
            print(Sum[i][j], end=' ');
            pass;
        print();
        pass;
    pass;

else:
    print("\nCannot add matrices!!\n");
    pass;
