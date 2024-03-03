def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Getting input from the user
num = int(input("Enter a number: "))

# Checking if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is", factorial(num))
