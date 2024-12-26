import random

# Step 1: Create a random list of numbers
def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Step 2: Implement Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Step 3: Print the sorted list
random_list = generate_random_list(10, 1, 100)  # List of 10 random numbers between 1 and 100
print("Original List:", random_list)

sorted_list = insertion_sort(random_list)
print("Sorted List:", sorted_list)
