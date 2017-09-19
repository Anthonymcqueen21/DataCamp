'''
Explore the baseball data
100xp
Because the mean and median are so far apart, you decide to complain to the MLB.
They find the error and send the corrected data over to you. It's again available
as a 2D Numpy array np_baseball, with three columns.

The Python script on the right already includes code to print out informative messages
with the different summary statistics. Can you finish the job?

Instructions
-The code to print out the mean height is already included. Complete the code for the
median height. Replace None with the correct code.
-Use np.std() on the first column of np_baseball to calculate stddev. Replace None with
the correct code.
-Do big players tend to be heavier? Use np.corrcoef() to store the correlation between
the first and second column of np_baseball in corr. Replace None with the correct code.
'''
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
