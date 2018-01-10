'''
Separate and summarize

Let's use population filtering to determine how the automobiles in the US differ from the global average and standard deviation. How the distribution of fuel efficiency (MPG) for the US differ from the global average and standard deviation?

In this exercise, you'll compute the means and standard deviations of all columns in the full automobile dataset. Next, you'll compute the same quantities for just the US population and subtract the global values from the US values.

All necessary modules have been imported and the DataFrame has been pre-loaded as df.

INSTRUCTIONS
100XP
-Compute the global mean and global standard deviations of df using the .mean() and .std() methods. Assign the results to global_mean and global_std.
-Filter the 'US' population from the 'origin' column and assign the result to us.
-Compute the US mean and US standard deviations of us using the .mean() and .std() methods. Assign the results to us_mean and us_std.
-Print the differences between us_mean and global_mean and us_std and global_std. This has already been done for you.
'''
import pandas as pd

df = pd.read_csv('../_datasets/auto-mpg.csv')

# Compute the global mean and global standard deviation: global_mean, global_std
global_mean = df.mean()
global_std = df.std()

# Filter the US population from the origin column: us
us = df[df['origin'] == 'US']

# Compute the US mean and US standard deviation: us_mean, us_std
us_mean = us.mean()
us_std = us.std()

# Print the differences
print(us_mean - global_mean)
print(us_std - global_std)