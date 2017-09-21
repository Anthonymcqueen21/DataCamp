'''
Relationship between Binomial and Poisson distributions
100xp
You just heard that the Poisson distribution is a limit of the Binomial distribution
for rare events. This makes sense if you think about the stories. Say we do a Bernoulli
trial every minute for an hour, each with a success probability of 0.1. We would do 60
trials, and the number of successes is Binomially distributed, and we would expect to get
about 6 successes. This is just like the Poisson story we discussed in the video, where
we get on average 6 hits on a website per hour. So, the Poisson distribution with arrival
rate equal to np approximates a Binomial distribution for n Bernoulli trials with probability
p of success (with n large and p small). Importantly, the Poisson distribution is often simpler
to work with because it has only one parameter instead of two for the Binomial distribution.
Let's explore these two distributions computationally. You will compute the mean and standard
deviation of samples from a Poisson distribution with an arrival rate of 10. Then, you will
compute the mean and standard deviation of samples from a Binomial distribution with parameters
n and p such that np=10.

Instructions
-Using the np.random.poisson() function, draw 10000 samples from a Poisson distribution with
a mean of 10.
-Make a list of the n and p values to consider for the Binomial distribution. Choose n =
[20, 100, 1000] and p = [0.5, 0.1, 0.01] so that np is always 10.
-Using np.random.binomial() inside the provided for loop, draw 10000 samples from a Binomial
distribution with each n, p pair and print the mean and standard deviation of the samples.
There are 3 n, p pairs: 20, 0.5, 100, 0.1, and 1000, 0.01. These can be accessed inside the
loop as n[i], p[i].
'''
import numpy as np

# Seed random number generator
np.random.seed(42)

# Draw 10,000 samples out of Poisson distribution: samples_poisson
samples_poisson = np.random.poisson(10, size=10000)

# Print the mean and standard deviation
print('Poisson:     ', np.mean(samples_poisson),
      np.std(samples_poisson))

# Specify values of n and p to consider for Binomial: n, p
n = [20, 100, 1000]
p = [0.5, 0.1, 0.01]

# Draw 10,000 samples for each n,p pair: samples_binomial
for i in range(3):
    samples_binomial = np.random.binomial(n[i], p[i], 10000)

    # Print results
    print('n =', n[i], 'Binom:', np.mean(samples_binomial),
          np.std(samples_binomial))
