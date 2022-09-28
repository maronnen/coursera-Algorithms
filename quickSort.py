#we count the number of comparisons made during quickSort, using three different rules for choosing a pivot
from statistics import median

#global variables for counting the number of comparisons
compareLeft,compareRight,compareMedian = 0,0,0

#parition an array by choosing the first entry as a pivot
def partitionLeft(arr, l, r):

	pivot = arr[l]
	
	i = l + 1
	
	for j in range(l + 1,r):
		if arr[j] <= pivot:
			(arr[i],arr[j]) = (arr[j],arr[i])
			i += 1
	
	(arr[i-1],arr[l]) = (pivot,arr[i-1])
	
	return i - 1
	
#partition an array by choosing the last entry as a pivot
def partitionRight(arr, l , r):
	pivot = arr[r-1]
	
	arr[r-1] = arr[l]
	arr[l] = pivot
	
	i = l + 1
	
	for j in range(l + 1,r):
		if arr[j] <= pivot:
			(arr[i],arr[j]) = (arr[j],arr[i])
			i += 1
	
	(arr[i-1],arr[l]) = (pivot,arr[i-1])
	
	return i - 1

def findMedian(arr,l,r):
	n = r - l
	a = arr[l]
	c = arr[r-1]
	
	if n % 2 == 0:
		b = arr[l + n//2 - 1]
	else:
		b = arr[l + n//2]
	
	return median([a,b,c])

#partition an array by choosing the median
def partitionMedian(arr, l,r):

	pivot = findMedian(arr,l,r)
	pivot_index = arr.index(pivot)
	 
	arr[pivot_index] = arr[l]
	arr[l] = pivot
	
	i = l + 1
	
	for j in range(l + 1,r):
		if arr[j] <= pivot:
			(arr[i],arr[j]) = (arr[j],arr[i])
			i += 1
	
	(arr[i-1],arr[l]) = (pivot,arr[i-1])
	
	return i - 1

#the quickSort algorithm
def quickSortLeft(arr,l,r):
	global compareLeft
	if l < r:
		partition_index = partitionLeft(arr,l,r)
		
		compareLeft += r - l -1
		
		quickSortLeft(arr,l,partition_index)
		quickSortLeft(arr,partition_index + 1, r)
		
def quickSortRight(arr,l,r):
	global compareRight
	if l < r:
		partition_index = partitionRight(arr,l,r)
		
		compareRight += r - l -1
		
		quickSortRight(arr,l,partition_index )
		quickSortRight(arr,partition_index + 1, r)
		
		
def quickSortMedian(arr,l,r):
	global compareMedian
	if l < r:
		partition_index = partitionMedian(arr,l,r)
		
		compareMedian += r - l -1
		
		quickSortMedian(arr,l,partition_index )
		quickSortMedian(arr,partition_index + 1, r)
		

#read the text file
filename = "QuickSort.txt"
data = open(filename)
content = data.read().splitlines()
N = len(content)
#make new array arr, whose entries are the entries of content converted to integers
arr = []
for i in range(N):
	arr.append(int(content[i]))

print("The length of the array is {}.\n".format(N))

#make 3 copies of arr to sort using different pivot choices
arrLeft = arr.copy()
arrRight = arr.copy()
arrMedian = arr.copy()

#quicksort all 
quickSortLeft(arrLeft,0,N)
print("Number of comparisons for quickSortLeft: {}".format(compareLeft))
#print("Sorted arrLeft: {}".format(arrLeft))
quickSortRight(arrRight,0,N)
print("Number of comparisons for quickSortRight: {}".format(compareRight))
#print("Sorted arrRight: {}".format(arrRight))
quickSortMedian(arrMedian, 0, N)
print("Number of comparisons for quickSortMedian: {}".format(compareMedian))