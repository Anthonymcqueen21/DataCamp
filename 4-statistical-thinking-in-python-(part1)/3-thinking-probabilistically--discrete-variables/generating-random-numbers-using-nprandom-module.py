'''
Generating random numbers using the np.random module
100xp

We will be hammering the np.random module for the rest of this course and its sequel.
Actually, you will probably call functions from this module more than any other while
wearing your hacker statistician hat. Let's start by taking its simplest function,
np.random.random() for a test spin. The function returns a random number between zero
and one. Call np.random.random() a few times in the IPython shell. You should see numbers
jumping around between zero and one.

In this exercise, we'll generate lots of random numbers between zero and one, and then
plot a histogram of the results. If the numbers are truly random, all bars in the histogram
should be of (close to) equal height.

You may have noticed that, in the video, Justin generated 4 random numbers by passing the
keyword argument size=4 to np.random.random(). Such an approach is more efficient than a
for loop: in this exercise, however, you will write a for loop to experience hacker
statistics as the practice of repeating an experiment over and over again.

Instructions
-Seed the random number generator using the seed 42.
-Initialize an empty array, random_numbers, of 100,000 entries to store the random numbers.
Make sure you use np.empty(100000) to do this.
-Write a for loop to draw 100,000 random numbers using np.random.random(), storing them in
the random_numbers array. To do so, loop over range(100000).
-Plot a histogram of random_numbers. It is not necessary to label the axes in this case
because we are just checking the random number generator. Hit 'Submit Answer' to show your plot.
'''
import numpy as np
import matplotlib.pyplot as plt

# Seed the random number generator
np.random.seed(42)

# Initialize random numbers: random_numbers
random_numbers = np.empty(100000)

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()
    print(random_numbers[i])


# Plot a histogram
_ = plt.hist(random_numbers)

# Show the plot
plt.show()
