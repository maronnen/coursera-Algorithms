#implementation of binary search algorithm.
#input: array of n numbers and a number
#ouput: whether or not the number is in the array, and if so where it is


#implementation of mergeSort algorithm for sorting an array of numbers from least to greates
def mergeSort(arr):
	n = len(arr)
	
	#check for base case
	if n > 1:
		n2 = n // 2
	
		#split array into left and right pieces
		L = arr[:n2]
		R = arr[n2 + 1:]
	
		#recursive call on left and right pieces
		mergeSort(L)
		mergeSort(R)
		
		#sort
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
			
#implementation of binarySearch on a sorted array
def binarySearch(arr, l, r, target):
	#l and r stand for the left and right indices of subarrays of arr
	
	#check for base case
	if r >= l:
		midpoint = l + (r - l) // 2
		
		#compare midpoint to target
		if arr[midpoint] == target:
			return midpoint
		#recur on left subarray
		elif target < arr[midpoint]:
			return binarySearch(arr, l, midpoint - 1, target)
		#recur on right subarray
		else: 
			return binarySearch(arr, midpoint + 1, r, target)
			
	#return -1 if target not found in arr
	else:
		return -1
	
#get input from user

print("This script will sort an array of numbers from least to greatest and then search the array for a given target number.\n")
#get length of array
while True:
	inData_length = input("Please enter the length of the array: ")
	try:
		array_length = int(inData_length)
		if array_length < 0:
			print("Length must be a positive integer. Try again.")
			continue
		break
	except ValueError:
		print("Length must be a positive integer. Try again.\n")

#get entries of the array
arr = []
for i in range(array_length):
	while True:
		inData_entry = input("Enter entry %d of the array: " % (i+1))
		try:
			x = float(inData_entry)
			break
		except ValueError:
			print("Array entries must be floats. Try again.\n")
	arr.append(x)
print("The array you entered is: \n")
print(arr)		

#get the target
while True:
	y = input("Please enter a target number: ")
	try:
		target = float(y)
		break
	except ValueError:
		print("Target must be a float. Try again.\n")
	
#sort the array
mergeSort(arr)

#search the sorted array for target
index = binarySearch(arr, 0, array_length - 1, target)

#tell whether target was found, and if so return the index it was found at


if index < 0:
	print("The target value %f was not found in the array.\n" % target)
else:
	print("The target value %f was found in the array at index %d.\n" % (target, index) )
	
	

	