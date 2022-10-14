# creating a heap in python!!

def PreserveHeapOrder(heap, index):
	i=index;

	while i>1:
		if heap[i]>heap[i//2]: # violation of heap order property!!
			heap[i], heap[i//2]=heap[i//2], heap[i]; # restoring heap order property!!

		i//=2;
	
	return;


heap=list();

size=int(input("enter the size of the array: "));

for i in range(size+1):
	heap.append(0);

print("enter elements:\n");
for i in range(1, size+1): # we are discarding the 0th index of the array(or rather the list!!)
	el=int(input(": "));
	heap[i]=el;
	PreserveHeapOrder(heap, i);

print("The heap is:");
for i in range(1, size+1):
	print(heap[i], end=' ');
print("\n");
