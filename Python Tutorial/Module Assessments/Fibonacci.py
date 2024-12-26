# Define required variables
n = int(input("Enter the number of Fibonacci numbers you want to generate: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Start the loop to generate Fibonacci numbers
print("Fibonacci sequence:")
for i in range(n):
    print(a)  # Print the current Fibonacci number
    a, b = b, a + b  # Update to the next Fibonacci numbers
