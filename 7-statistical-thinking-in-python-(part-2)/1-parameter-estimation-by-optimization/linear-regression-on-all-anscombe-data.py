'''
Linear regression on all Anscombe data

Now, to verify that all four of the Anscombe data sets have the same slope and intercept from a 
linear regression, you will compute the slope and intercept for each set. The data are stored in 
lists; anscombe_x = [x1, x2, x3, x4] and anscombe_y = [y1, y2, y3, y4], where, for example, x2 and y2 
are the x and y values for the second Anscombe data set.
'''
# Iterate through x,y pairs
for x, y in zip(anscombe_x, anscombe_y):
    # Compute the slope and intercept: a, b
    a, b = np.polyfit(x, y, 1)

    # Print the result
    print('slope:', a, 'intercept:', b)
