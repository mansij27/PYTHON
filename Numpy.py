import numpy as np

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

print("Initial Array: ")
print(arr)

sliced_arr = arr[:2, ::2]
print("Array with first 2 rows and alternate columns(0 and 2):\n", sliced_arr)

# Adding 1 to every element
print("Adding 1 to every element:", arr + 1)

# Subtracting 2 from each element
print("\nSubtracting 2 from each element:", arr - 2)

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[4, 3],
              [2, 1]])

# sum of array elements performing Unary operations
print("\nSum of all array elements: ", a.sum())

# Adding two arrays performing Binary operations
print("\nArray sum:\n", a + b)