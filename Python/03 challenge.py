name = input("Please enter your name: ")
number = input("Please enter a number: ")

number = int(number)

print("Hey name!".format(name))
print("The number {}...")

if number % 3 == 0 and number % 5 == 0: # multiple conditions placed in IF CONDITION by using OR and AND. However, in this case, AND is required
  print("is a FizzBuzz number.") # this conditions must go first because REPL doesn't reaches this condition if it's placed at last.
elif number % 3 == 0:
  print("is a Fizz number.")
elif number % 5 == 0:
  print("is a Buzz number.")
else:
  print("is neither a fizzy or a buzzy number.")
