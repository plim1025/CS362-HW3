def isLeapYear(num):
	if num % 4 != 0:
		return False
	if num % 100 != 0:
		return True
	return num % 400 == 0

num = input("Enter a number to test: ")
if not num.isdigit():
	print("Invalid input, not an integer")
	exit()
if(isLeapYear(int(num))):
	print(num, "is a leap year")
else:
	print(num, "is not a leap year")