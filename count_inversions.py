

def mergeSort(arr, temp_arr, l, r):
	inv_count = 0
	
	if l < r:
		midpoint = (l + r)//2
		inv_count += mergeSort(arr, temp_arr, l, midpoint)
		inv_count += mergeSort(arr, temp_arr, midpoint + 1, r)
		
		inv_count += merge(arr, temp_arr, l, midpoint, r)
	return inv_count
	
def merge(arr, temp_arr, l, midpoint, r):
	i = l
	j = midpoint + 1
	k = l
	inv_count = 0
	
	while i <= midpoint and j <= r:
		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			temp_arr[k] = arr[j]
			j += 1
			k += 1
			inv_count += (midpoint - i + 1)
			
	while i <= midpoint:
		temp_arr[k] = arr[i]
		i += 1
		k += 1
		
	while j <= r:
		temp_arr[k] = arr[j]
		j += 1
		k += 1 
		
	for m in range(l, r + 1):
		arr[m] = temp_arr[m]
		
	return inv_count


#get an array to count the inversions in
#we have to read the given txt file

#read the file
filename = "IntegerArray.txt"
data = open(filename)
content = data.read().splitlines()
for i in range(len(content)):
	content[i] = int(content[i])
arr = content
n = len(arr)
countInversions = mergeSort(arr, [0] * n, 0, n - 1)
print("The number of inversions is %d.\n" % countInversions)