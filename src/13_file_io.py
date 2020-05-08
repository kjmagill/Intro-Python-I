"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# My updated solution
with open("foo.txt") as f:
  for line in f:
    print(line)

# # My original solution
# with open('src/foo.txt') as f:
#   print(f.read())
# f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# with open('src/bar.txt', 'w') as b:
#   lines = ['Hello world...\n', 'Welcome to my Python-I project\n', 'Have a great day!\n']
#   b.writelines(lines)
# b.close()

# with open('bar.txt') as b:
#   print(b.read())
# b.close()

# My updated solution
file = open('bar.txt','w')
file.write("""Hello world...\n', 'Welcome to my Python-I project.\n', 'Have a great day!\n""")
file.close()

# # My original solution
# file = open('src/bar.txt','w')
# lines = ['Hello world...\n', 'Welcome to my Python-I project.\n', 'Have a great day!\n']
# file.writelines(lines)
# file.close()