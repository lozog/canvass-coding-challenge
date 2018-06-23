# helper function for evenDigits
# given a string representation of a number, returns true if all the digits
# are even, false otherwise
def checkAllDigitsEven(strnum):
	for char in strnum:
		try:
			if int(char) % 2 != 0:
				return False
		except ValueError: # handles negative sign
			continue
	return True

# given a lower and upper bound, prints all numbers between these bounds where
# each digit of the numbers is even
def evenDigits(lower, upper):

	# array of even digits
	# I know there are only 5 even digits, but this can be easily changed to the odd digits
	evens = [x for x in range(10) if x%2 == 0]

	for num in range(lower, upper+1):
		strnum = str(num)
		if not checkAllDigitsEven(strnum):
			continue
		print("{},".format(num), end='')

	# remove the trailing comma and end with a newline
	# the space after the \b is on purpose
	print("\b ") 

evenDigits(1000, 3000)