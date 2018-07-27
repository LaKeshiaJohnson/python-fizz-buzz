number = int(raw_input("Please enter a number: "))

# values should be stored in booleans
# If the number is divisible by 3, print "is a Fizz number"
# If the number is divisible by 5, print "is a Buzz number"
# If the number is divisible by both 3 and 5, print is a FizzBuzz number"
# Otherwise, print "is neither a fizzy or buzzy number"

is_fizz = number % 3 == 0
is_buzz = number % 5 == 0

if (is_fizz and is_buzz):
	print("{} is a FizzBuzz number.".format(number))
elif (is_fizz):
	print("{} is a Fizz number.".format(number))
elif (is_buzz):
	print("{} is a Buzz number.".format(number))
else:
	print("{} is neither a fizzy or buzzy number.".format(number))
