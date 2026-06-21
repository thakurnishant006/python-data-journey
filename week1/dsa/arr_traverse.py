"""Array Traversal

Traversal means visiting each element of an array/list one by one
to perform an operation such as searching, counting, updating,
finding max/min, sum, filtering, etc.

Syntax:

for item in arr:
    # perform operation

OR

for i in range(len(arr)):
    # use index
    arr[i]

Examples:
- Find maximum value
- Find minimum value
- Calculate sum
- Count even numbers
- Search for an element
- Create a filtered list

Time Complexity:
O(n) because every element is visited once.

"""

# Find the maximum

arr = [5, 12, 3, 20, 8]
max_num = arr[0]
for i in range(1,len(arr)):
    if arr[i] > max_num:
        max_num = arr[i]
        
print(max_num)

# find even
arr = [4, 7, 10, 13, 16, 19]
count = 0
for i in arr:
    if i % 2 == 0:
        count +=1
print(count)

# Traverse the array and create a new list containing only numbers greater than 5
arr = [2, 8, 1, 9, 4, 7]
new = []
for i in arr:
    if i > 5:
        new.append(i)

print(new)

# Find the second largest element.
arr = [10, 5, 20, 8, 15,20]
max_val = float('-inf')
sec_val = float('-inf')
for i in range(len(arr)):
    if arr[i] > max_val:
        sec_val = max_val
        max_val = arr[i]
    elif arr[i] < max_val and arr[i] > sec_val:
        sec_val = arr[i]
print(sec_val)