import random

# Generate a random list of 10 numbers
numbers = random.sample(range(1, 100), 10)
print("Original list:", numbers)

# Implementing Bubble Sort algorithm
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# Sorting the list using Bubble Sort
sorted_numbers = bubble_sort(numbers.copy())
print("Sorted list:", sorted_numbers)
