import math

# Take input from the user and assign it to a variable called radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference and area of the circle
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Print the results
print(f"Circumference: {circumference}")
print(f"Area: {area}")
