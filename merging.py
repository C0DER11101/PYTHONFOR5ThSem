# Merging two arrays!


def Merge(a1, a2, size1, size2, result):
    #--- sort a1 ---
    for i in range(size1):
        for j in range(size1-1):
            if a1[j]>a1[j+1]:
                a1[j], a1[j+1]=a1[j+1], a1[j];

    #--- sort a2 ---
    for i in range(size2):
        for j in range(size2-1):
            if a2[j]>a2[j+1]:
                a2[j], a2[j+1]=a2[j+1], a2[j];


    # --- Merging a1 and a2 ---

    a1Ind=0;
    a2Ind=0;

    while a1Ind!=size1 and a2Ind!=size2:
        if a1[a1Ind]<=a2[a2Ind]:
            result.append(a1[a1Ind]);
            a1Ind+=1;

        elif a2[a2Ind]<a1[a1Ind]:
            result.append(a2[a2Ind]);
            a2Ind+=1;


    if a1Ind==size1:
        if a2Ind!=size2:
            while a2Ind!=size2:
                result.append(a2[a2Ind]);
                a2Ind+=1;
    elif a2Ind==size2:
        if a1Ind!=size1:
            while a1Ind!=size1:
                result.append(a1[a1Ind]);
                a1Ind+=1;


result=list();
a1=list();
a2=list();

size1=int(input("enter size of the first array: "));
size2=int(input("enter size of the second array: "));

print("enter elements into the first array: ");
for i in range(size1):
    el=int(input());
    a1.append(el);

print("enter elements into the second array: ");
for i in range(size2):
    el=int(input());
    a2.append(el);

Merge(a1, a2, size1, size2, result);

print("you arrays after sorting:\n");

print(a1);
print(a2);

print("\nThis the merged array:\n\n");
print(result);
