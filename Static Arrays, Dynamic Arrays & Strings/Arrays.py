# Python array implementation are very trivial compared to other languages like C/C++ or Java.
# Python provides a built-in list data structure that can be used as a dynamic array.

# Dynamic Arrays (Lists in Python)

A = [1,2,3,4,5]

print("Initial Array:", A)

# Accessing elements - O(1) time complexity
print("First element:", A[0])  # Output: 1
print("Last element:", A[-1])   # Output: 5

# Unsorted Search - O(n) time complexity
def unsorted_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

index = unsorted_search(A, 3)
print("Index of 3 in unsorted array:", index)  # Output: 2

# Insertion at the end - *O(1) amortized time complexity
A.append(6)
print("Array after insertion at the end:", A)  # Output: [1, 2, 3, 4, 5, 6]

# Insert at middle - O(n) time complexity
A.insert(2, 10)  # Insert 10 at index 2
print("Array after insertion at index 2:", A)  # Output: [1, 2, 10, 3, 4, 5, 6]

# Deletion from end - O(1) time complexity
A.pop()
print("Array after deletion from end:", A)  # Output: [1, 2, 10, 3, 4, 5]

# Deletion from middle - O(n) time complexity
A.pop(2)  # Remove item at index 2
print("Array after deletion from index 2:", A)  # Output: [1, 2, 3, 4, 5]

print("Note - Copying and resizing happens automatically in "
    "Python lists with a time complexity of O(n) in the worst case.")