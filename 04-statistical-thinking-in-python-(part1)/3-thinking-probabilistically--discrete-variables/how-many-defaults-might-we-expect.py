'''
How many defaults might we expect?
100xp

Let's say a bank made 100 mortgage loans. It is possible that anywhere between
0 and 100 of the loans will be defaulted upon. You would like to know the probability
of getting a given number of defaults, given that the probability of a default is
p = 0.05. To investigate this, you will do a simulation. You will perform 100 Bernoulli
trials using the perform_bernoulli_trials() function you wrote in the previous exercise
and record how many defaults we get. Here, a success is a default. (Remember that the
word "success" just means that the Bernoulli trial evaluates to True, i.e., did the loan
recipient default?) You will do this for another 100 Bernoulli trials. And again and again
until we have tried it 1000 times. Then, you will plot a histogram describing the probability
of the number of defaults.

Instructions
-Seed the random number generator to 42.
-Initialize n_defaults, an empty array, using np.empty(). It should contain 1000 entries,
since we are doing 1000 simulations.
-Write a for loop with 1000 iterations to compute the number of defaults per 100 loans using
the perform_bernoulli_trials() function. It accepts two arguments: the number of trials n -
in this case 100 - and the probability of success p - in this case the probability of a default,
which is 0.05. On each iteration of the loop store the result in an entry of n_defaults.
-Plot a histogram of n_defaults. Include the normed=True keyword argument so that the height of
the bars of the histogram indicate the probability.
-Show your plot.
'''
import numpy as np
import matplotlib.pyplot as plt


def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success


# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100, 0.05)


# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed=True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')

# Show the plot
plt.show()
