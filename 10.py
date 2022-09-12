# WRITE A PROGRAM IN PYTHON TO FIND THE SUMMATION OF 2D MATRICES
# Get size of matrix
row_size=int(input("enter the row size of the matrix: "))
col=int(input("enter the column size of the matrix: "))

matrix=[]
# taking input of the matrix
print("enter the matrix element:");

for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
    
#calculate sum of given matrix elements
    
sum=0

for i in range(0, row_size):
    for j in range(0, col):
        sum+=matrix[i][j]
        
#display the sum of the given matrix elements
print("Sum of the given matrix elements is: ", sum)