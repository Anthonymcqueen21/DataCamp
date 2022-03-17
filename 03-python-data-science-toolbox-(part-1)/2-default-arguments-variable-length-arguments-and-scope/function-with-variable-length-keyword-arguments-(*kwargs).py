'''
Function with variable-length keyword arguments (**kwargs)
100xp

Let's push further on what you've learned about flexible arguments - you've used *args,
you're now going to use **kwargs! What makes **kwargs different is that it allows you to
pass a variable number of keyword arguments to functions. Recall from the previous video
that, within the function definition, kwargs is a dictionary.

To understand this idea better, you're going to use **kwargs in this exercise to define a
function that accepts a variable number of keyword arguments. The function simulates a
simple status report system that prints out the status of a character in a movie.

Instructions
-Complete the function header with the function name report_status. It accepts a single
flexible argument **kwargs.
-Iterate over the key-value pairs of kwargs to print out the keys and values, separated
by a colon ':'.
-In the first call to report_status(), pass the following keyword-value pairs: name="luke",
affiliation="jedi" and status="missing".
-In the second call to report_status(), pass the following keyword-value pairs: name="anakin",
affiliation="sith lord" and status="deceased".
'''
# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name='luke', affiliation='jedi', status='missing')

# Second call to report_status()
report_status(name='anakin', affiliation='sith lord', status='deceased')
