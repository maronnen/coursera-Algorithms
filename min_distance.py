#implementation of divide and conquer algorithm for finding the minimum distance between a pair of points
#out of a set of points in the plane
import math

#function for computing the distance between two points
def dist(p,q):
	return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
	
#function for finding the minimum distance between a pair of points in a small set of points
def minDist_small(arr, num_points):
	min_distance = float('inf')
	n = num_points
	
	if n == 2:
		min_distance = dist(arr[0], arr[1])
	else:
		min_distance = min(dist(arr[0],arr[1]), dist(arr[0],arr[2]), dist(arr[1],arr[2]))
	return min_distance
	
#mergeSort algorithm, sorting based on y-coordinate
def mergeSort(arr):
	n = len(arr)
	if n > 1:
		n2 = n // 2
	
		L = arr[:n2]
		R = arr[n2:]
	
		mergeSort(L)
		mergeSort(R)
	
		i = j = k = 0
	
		while i < len(L) and j < len(R):
			if L[i][1] <= R[j][1]:
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
		

#function for finding nearest pair within a strip of width 2d
def nearest_in_strip(strip, num_points, d):
	min_val = d
	
	for i in range(num_points):
		j = i + 1
		while j < num_points and (strip[j][1] - strip[i][1]) < min_val:
			min_val = dist(strip[i], strip[j])
			j += 1
	return min_val

#function for finding nearest pair of points
#it will call itself recursively
def nearestPair(arr, num_points):

	n = num_points
	n2 = n // 2
	
	#base cases
	if n <= 3:
		return minDist_small(arr,n)
	
	#split array into Left and Right pieces
	L = arr[:n2]
	R = arr[n2 + 1:]
	
	#recusrion
	dl = nearestPair(L, n2)
	dr = nearestPair(R, n - n2 - 1)
	
	#let d be the minimum of dl and dr
	d = min(dl,dr)
	
	#Consider points in the strip of width 2d about the vertical line separating L and R
	strip = []
	for i in range(n):
		if abs(arr[i][0] - arr[n2][0]) < d:
			strip.append(arr[i])
			
	#sort strip according to y-coordinate
	mergeSort(strip)
	min_val = min(d, nearest_in_strip(strip, len(strip), d))
	
	return min_val

#Get data from the user
#input prompt symbol
prompt = "> "

#get the number of points from the user
#the input must be a positive integer, greater than 1
while True:
	print("How many points?")
	in_number = input(prompt)
	try: 
		N = int(in_number)
		if N < 0:
			print("Entry must be a positive integer. Try again.\n")
			continue
			
		if N == 1:
			print("Entry must be a positive integer greater than 1. Try again.\n")
			continue
		break
	except ValueError:
		print("Not a positive integer. Try again.\n")
		
#get the list of points from the user
points = []
for i in range(N):
	while True:
		print("Enter x-coordinate of point %d" % (i+1))
		in_x = input(prompt)
		try:
			x = float(in_x)
			break
		except ValueError:
			print("Entry must be a float.")
	while True:
		print("Enter y-coordinate of point %d" % (i+1))
		in_y = input(prompt)
		try:
			y = float(in_y)
			break
		except ValueError:
			print("Entry must be a float.")
	points.append([x,y])

print("You have entered %d points. They are:\n" % N)	
print(points, "\n")

#run the algorithm on the user data, returning the nearest pair
min_distance = nearestPair(points, N)
print("The minimum distance between a pair of points in the given set of points is %f.\n" % min_distance)