# Take input from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform calculations
sum_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number

# Handle division by zero
if second_number != 0:
    division_result = first_number / second_number
else:
    division_result = "Undefined (division by zero)"

# Print results
print(f"Sum: {sum_result}")
print(f"Subtraction: {subtraction_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division: {division_result}")
