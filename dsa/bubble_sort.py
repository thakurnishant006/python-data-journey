# Bubble Sort

# Bubble Sort repeatedly compares adjacent elements.
# If they are in the wrong order, they are swapped immediately.
# After each pass, the largest element "bubbles" to the end.
#
# Time Complexity:
# Best Case: O(n)
# Average Case: O(n²)
# Worst Case: O(n²)
#
# Suitable for:
# - Learning sorting concepts
# - Small datasets
#
# Not suitable for:
# - Large datasets

"""
Pseudo Code

1. Loop through the array.
2. Create a second loop starting from index 1.
3. Compare adjacent elements:
       arr[j] and arr[j-1]
4. If current element is smaller:
       swap immediately
5. After each pass, the largest element reaches
   its correct position at the end.
6. Reduce comparisons using:
       len(arr) - i
   because the right side is already sorted.
"""

arr = [5,3,67,8,9,2,1]

for i in range(len(arr)):
    for j in range(1, len(arr) - i):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]

print(arr)