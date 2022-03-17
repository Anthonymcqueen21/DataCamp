'''
Generating many bootstrap replicates

The function bootstrap_replicate_1d() from the video is available in your namespace. Now you'll write
another function, draw_bs_reps(data, func, size=1), which generates many bootstrap replicates from the
data set. This function will come in handy for you again and again as you compute confidence intervals
and later when you do hypothesis tests.

For your reference, the bootstrap_replicate_1d() function is provided below:

def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))
INSTRUCTIONS
100XP
-Define a function with call signature draw_bs_reps(data, func, size=1).
-Using np.empty(), initialize an array called bs_replicates of size size to hold all of the bootstrap
replicates.
-Write a for loop that ranges over size and computes a replicate using bootstrap_replicate_1d(). Refer
to the exercise description above to see the function signature of bootstrap_replicate_1d(). Store the
replicate in the appropriate index of bs_replicates.
-Return the array of replicates bs_replicates. This has already been done for you.
'''
def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates
