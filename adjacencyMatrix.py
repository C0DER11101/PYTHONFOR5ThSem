numV=int(input("enter number of vertices: "));

maxEdge=numV*(numV-1);

print(f"Directed graph will have {maxEdge} edges!!\n\n");

adjMat=[];

for i in range(numV):
    for j in range(numV):
        print("enter edge: ");
        iV=int(input(":"));
            