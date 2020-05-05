"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print('Should be 4:', a[1])

# Output the second-to-last element: 9
print('Should be 9:', a[-2])

# Output the last three elements in the array: [7, 9, 6]
print('Should be [7, 9, 6]:', a[-3:])

# Output the two middle elements in the array: [1, 7]
print('Should be [1, 7]:', a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
print('Should be [4, 1, 7, 9, 6]:', a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print('Should be [2, 4, 1, 7, 9]:', a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print('Should be "world":', s[7:12])