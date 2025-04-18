# Step 1: Define the factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Step 2 & 3: Call the function with a sample number and print the output
number = int(input("Enter a number to calculate its factorial: "))
fact = factorial(number)
print(f"The factorial of {number} is: {fact}")
