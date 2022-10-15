# performing heap sort in python!!

def buildHeap(heap, size):
	# take the last non-leaf node!!
	index=(size-1)//2;

	while index>=1:
		i=index;

		while (2*i < size) and (heap[i] < heap[2*i] or heap[i] < heap[2*i+1]):
			if heap[2*i] > heap[2*i+1]:
				if heap[i] <= heap[2*i]:
					heap[i], heap[2*i]=heap[2*i], heap[i];
					i*=2;
			elif heap[2*i+1] > heap[2*i]:
				if heap[i] < heap[2*i+1]:
					heap[i], heap[2*i+1]=heap[2*i+1], heap[i];
					i=2*i+1;
		
		index-=1;

	return;


heap=list();
size=int(input("enter size: "));

for i in range(size+1):
	heap.append(0);

print("enter elements: ");

for i in range(1, size+1):
	heap[i]=int(input(": "));


buildHeap(heap, size+1);

print("Heap building complete!! Here is the heap: ");

for i in range(1, size+1):
	print(heap[i], end=' ');
print();
