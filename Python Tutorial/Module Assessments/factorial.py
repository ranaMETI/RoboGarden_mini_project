def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Take input from the user
while True:
    try:
        number = int(input("Enter a non-negative integer (or -1 to exit): "))
        if number == -1:
            print("Exiting the program. Goodbye!")
            break
        elif number < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"The factorial of {number} is {factorial(number)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
