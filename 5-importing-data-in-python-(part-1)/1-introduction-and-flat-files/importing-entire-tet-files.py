'''
Importing entire text files
100xp

In this exercise, you'll be working with the file moby_dick.txt. It is a text
file that contains the opening sentences of Moby Dick, one of the great American
novels! Here you'll get experience opening a text file, printing its contents to
the shell and, finally, closing it.

Instructions
-Open the file moby_dick.txt as read-only and store it in the variable file. Make
sure to pass the filename enclosed in quotation marks ''.
-Print the contents of the file to the shell using the print() function. As Hugo
showed in the video, you'll need to apply the method read() to the object file.
-Check whether the file is closed by executing print(file.closed).
-Close the file using the close() method.
-Check again that the file is closed as you did above.
'''
# Open a file: file
file = open('../_datasets/moby_dick.txt', mode='r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)
