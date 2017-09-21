'''
The np.random module and Bernoulli trials
100xp
You can think of a Bernoulli trial as a flip of a possibly biased coin. Specifically, each coin flip has a probability p
 of landing heads (success) and probability 1−p
 of landing tails (failure). In this exercise, you will write a function to perform n Bernoulli trials, perform_bernoulli_trials(n, p), which returns the number of successes out of n Bernoulli trials, each of which has probability p of success. To perform each Bernoulli trial, use the np.random.random() function, which returns a random number between zero and one.

Instructions
-Define a function with signature perform_bernoulli_trials(n, p).
    -Initialize to zero a variable n_success the counter of Trues, which are Bernoulli trial successes.
    -Write a for loop where you perform a Bernoulli trial in each iteration and increment the number of success if the result is True. Perform n iterations by looping over range(n).
    -To perform a Bernoulli trial, choose a random number between zero and one using np.random.random(). If the number you chose is less than p, increment n_success (use the += 1 operator to achieve this).
    -The function returns the number of successes n_success.
'''
import numpy as np


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


print(perform_bernoulli_trials(10000, 0.65))
