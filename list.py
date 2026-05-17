import array as arr
from hashlib import new

arr1 = arr.array('i', [1, 2, 3, 4, 5])
arr2 = arr.array(arr1.typecode, (n for n in arr1))  # Create a copy of arr1

arr1[2] = 10

print(arr1)  # Output: array('i', [1, 2, 10, 4, 5])
print(arr2)  # Output: array('i', [1, 2, 3, 4, 5])
 
    