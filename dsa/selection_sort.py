# Selection Sort

# Used for small datasets and for learning sorting algorithms.
# Not recommended for large datasets because of O(n²) time complexity.

# Idea:
# Assume the current position contains the smallest value.
# Search the remaining unsorted portion of the array.
# If a smaller value is found, remember its index.
# After the search is complete, swap the smallest value into the current position.
# Repeat until the array is sorted.

# Time Complexity: O(n²)
# Space Complexity: O(1)

"""
Pseudo Code:

1. Loop through each index i in the array.
2. Assume the current index contains the minimum value:
       min_idx = i
3. Search the remaining array:
       for j in range(i + 1, len(arr))
4. If a smaller value is found:
       min_idx = j
5. After the search is complete, swap:
       arr[i], arr[min_idx] = arr[min_idx], arr[i]
6. Repeat until the array is sorted.
"""

arr = [2,5,7,1,2,4,5,9,6,5]

# Sort the array first using Selection Sort
for i in range(len(arr)):
    min_num = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_num]:
            min_num = j
    arr[i], arr[min_num] = arr[min_num], arr[i]

# Since the array is sorted, duplicates will be adjacent
unique = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:   # Compare with previous element
        unique.append(arr[i])

print(unique)

"""
If the array is NOT sorted:

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)

Reason:
Duplicates may be anywhere in the array, so we must check
whether the value already exists in unique.
"""