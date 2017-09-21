'''
Was 2015 anomalous?
100xp

1990 and 2015 featured the most no-hitters of any season of baseball (there were seven).
Given that there are on average 251/115 no-hitters per season, what is the probability of
having seven or more in a season?

Instructions
-Draw 10000 samples from a Poisson distribution with a mean of 251/115 and assign to n_nohitters.
-Determine how many of your samples had a result greater than or equal to 7 and assign to n_large.
-Compute the probability, p_large, of having 7 or more no-hitters by dividing n_large by the total
number of samples (10000).
-Hit 'Submit Answer' to print the probability that you calculated.
'''
import numpy as np

# Seed random number generator
np.random.seed(42)

# Draw 10,000 samples out of Poisson distribution: n_nohitters
n_nohitters = np.random.poisson((251 / 115), size=10000)

# Compute number of samples that are seven or greater: n_large
n_large = np.sum(n_nohitters >= 7)

# Compute probability of getting seven or more: p_large
p_large = n_large / 10000

# Print the result
print('Probability of seven or more no-hitters:', p_large)
