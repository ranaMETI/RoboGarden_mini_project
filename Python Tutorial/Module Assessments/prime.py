# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Taking input from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Loop through the range and check for prime numbers
for num in range(start, end + 1):
    if is_prime(num):
        print(num)  # Print the prime number
