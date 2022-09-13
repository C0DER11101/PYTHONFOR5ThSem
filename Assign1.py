# CSE-28/20

matrix1=[];
matrix2=[];

print("MATRIX-1:\n");
row1=int(input("enter number of rows: "));
col1=int(input("enter number of columns: "));

print("MATRIX-2:\n");
row2=int(input("enter number of rows: "));
col2=int(input("enter number of columns: "));

if col1 != row2:
    print("Cannot multiply matrices!!\n\n");
    
    
else:
    
    print("MATRIX-1:\n");
    print("enter elements:\n\n");
    for i in range(row1):
        matrix1.append([int(j) for j in input().split()]);
        
    print("MATRIX-2:\n");
    print("enter elements:\n\n");
    for i in range(row2):
        matrix2.append([int(j) for j in input().split()]);
        
        
    #print("here is the matrix:", matrix1);  # prints a list of lists!!
    
    
    print("MATRIX-1:\n");
    for i in range(row1):
        for j in range(col1):
            print(matrix1[i][j], end=" ");
            
        print("\n");
        
    print("MATRIX-2:\n");
    for i in range(row2):
        for j in range(col2):
            print(matrix2[i][j], end=" ");
            
        print("\n");
        
        
    print("\n\nMATRIX1 x MATRIX2:\n\n");
        
    # multiplying two matrices!!
    
    for i in range(row1):
        for j in range(col2):
            sumMat=0;
            
            for k in range(col1):
                sumMat+=matrix1[i][k]*matrix2[k][j];
                
            print(sumMat, end=" ");
            
        print("\n");