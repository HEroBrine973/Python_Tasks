import math  # Import the math module

# Step 1: Ask the user for a number
num = float(input("Enter a positive number: "))

# Step 2: Perform calculations using math module
if num > 0:
    square_root = math.sqrt(num)
    natural_log = math.log(num)
    sine_value = math.sin(num)

    # Step 3: Display the results
    print(f"\nResults for the number {num}:")
    print(f"Square Root: {square_root}")
    print(f"Natural Logarithm (ln): {natural_log}")
    print(f"Sine: {sine_value}")
else:
    print("Please enter a number greater than 0 for logarithm and square root.")
