# Merge Sort Algorithm in Python

# Function to merge two halves
def merge(left, right):
    result = []
    i = j = 0
    
    # Merge the two halves in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Merge Sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort each half and merge
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted)

# Test the merge sort function
arr = [45, 84, 74, 71, 99, 18, 82, 52, 17, 29]
sorted_arr = merge_sort(arr)
print("Sorted List:", sorted_arr)
