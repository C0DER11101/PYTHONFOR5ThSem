# Merge Sort in Python!!

def mergeSort(array, left, right):
	if right>1: # if the length of the array is greater than 1 then continue splitting!!
		# Step 1: divide the array into equal halves!!
		mid=right//2;
		Left=array[:mid];
		Right=array[mid:];
		mergeSort(Left, left,len(Left)); # merge sort the left half
		mergeSort(Right, mid, len(Right)); # merge sort the right half

		iL=iR=iM=0;
		while iL < len(Left) and iR < len(Right):
			if Left[iL] <= Right[iR]:
				array[iM]=Left[iL];
				iL+=1;
			elif Right[iR] < Left[iL]:
				array[iM]=Right[iR];
				iR+=1;
			iM+=1;

		while iL<len(Left):
			array[iM]=Left[iL];
			iM+=1;
			iL+=1;

		while iR<len(Right):
			array[iM]=Right[iR];
			iM+=1;
			iR+=1;
	return;

array=list();
size=int(input("enter size of the array: "));

print("enter elements into the array: ");

for i in range(size):
	e=int(input(":"));
	array.append(e);
right=len(array);
mergeSort(array, 0, right);

print(f"the sorted array is: {array}\n");
