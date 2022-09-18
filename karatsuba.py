#This scipt implements the Karatsuba algorithm for multiplication of two integers.
#The user inputs two integers, which may be negative, and returns their product

#addZeros takes in a string representing a positive integer, how many zeros to add, and whether or not
#to add zeros on the left or right. It then adds zeros to the left or right of the string
def addZeros(numString, zeros, left=True):
	for i in range(zeros):
		if left:
			numString = '0' + numString
		else:
			numString = numString + '0'
	return numString

#karatsuba takes in integers x and y of the same number of digits, a power of 2, and returns their produc
#using the karatsuba algorithm
def karatsuba(x, y):
	
	x = str(x)
	y = str(y)
	
	lenx = len(x)
	leny = len(y)
	
	#booleans to keep track of whether or not x and y are negative
	xNeg = False
	yNeg = False
	if int(x) < 0:
		xNeg = True
		x = x[1:]
	if int(y) < 0:
		yNeg = True
		y = y[1:]
	
	#base case
	if lenx == 1 or leny == 1:
		return int(x) * int(y)
		
	#if x,y have different lengths, pad one of them by adding zeros on the front
	if lenx < leny:
		x = addZeros(x,leny - lenx)
			
	if leny < lenx:
		y = addZeros(y,lenx - leny)

	#count how many digits are in x and y
	n = len(x)
	n2 = n // 2
	
	#if n is odd, add 1 to n//2
	if (n % 2) != 0:
		n2 += 1
	
	#get integers a,b,c,d
	#a = first n/2 digits of x
	#b = last n/2 digits of x
	#c = first n/2 digits of y
	#d = last n/2 digits of y
	a = int(x[:n2])
	b = int(x[n2:])
	c = int(y[:n2])
	d = int(y[n2:])
	
	
	#compute ac, bd, and (10^n/2 a + b)(10^n/2 c + d), and then ad + bc
	ac = karatsuba(a,c)
	bd = karatsuba(b,d)
	ab_cd  = karatsuba(a + b, c + d)
	ad_plus_bc = ab_cd - ac - bd
	
	#compute the product of x and y
	AC = int(addZeros(str(ac), 2 * (n - n2), False))
	AD_PLUS_BC = int(addZeros(str(ad_plus_bc), n - n2, False))
	product = AC + AD_PLUS_BC + bd
	
	#check if we should make product negative or not
	if xNeg ^ yNeg:
		product *= -1

	return product


#Get inputs from user
#test if inputs are positive integers
print("Please enter two positive integers x and y: \n")

while True:
	x = input("Enter integer x: \n")
	try:
		int(x)
		break
	except ValueError:
		print("That is not an integer.")
		
while True:
	y = input("Enter integer y: \n")
	try:
		int(y)
		break
	except ValueError:
		print("That is not an integer.")

#perform the karatsuba multiplication of x and y
result = karatsuba(x,y)
print("Result: ", result, "\n")

