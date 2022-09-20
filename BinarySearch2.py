import time

def Binary(arr, size, el):
    low=0;
    high=size-1;
    
    while low<=high:
        mid=int((low+high)/2);
        
        if arr[mid]==el:
            return el;
        
        elif arr[mid]<el:
            low=mid+1;
        else:
            high=mid-1;
        
    
    return 0;
    


arr=list();

size=int(input("enter size of the array: "));

for i in range(size):
    el=int(input(f"element {i+1}: "));
    arr.append(el);
    

if __name__=="__main__":
    element=int(input("enter element to be searched: "));
    s=time.time();
    result=Binary(arr, size, element);
    e=time.time();
    
    if result!=0:
        print(f"{element} found in the array!!\n\n");
        
    else:
        print(f"{element} not found in the array!!\n\n");
        
    print(e-s);