'''
Importing text files line by line
100xp

For large files, we may not want to print all of their content to the shell:
you may wish to print only the first few lines. Enter the readline() method,
which allows you to do this. When a file called file is open, you can print out
the first line by executing file.readline(). If you execute the same command again,
the second line will print, and so on.

In the introductory video, Hugo also introduced the concept of a context manager.
He showed that you can bind a variable file by using a context manager construct:

with open('huck_finn.txt') as file:

While still within this construct, the variable file will be bound to open('huck_finn.txt');
thus, to print the file to the shell, all the code you need to execute is:

with open('huck_finn.txt') as file:
    print(file.read())

You'll now use these tools to print the first few lines of moby_dick.txt!

Instructions
-Open moby_dick.txt using the with context manager and the variable file.
-Print the first three lines of the file to the shell by using readline() three
times within the context manager.
'''
# Read & print the first 3 lines
with open('../_datasets/moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
