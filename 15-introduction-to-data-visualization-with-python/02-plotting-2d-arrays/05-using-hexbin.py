'''
Using hexbin()

The function plt.hist2d() uses rectangular bins to construct a two dimensional histogram. As an alternative, the function plt.hexbin() uses hexagonal bins. The underlying algorithm (based on this article from 1987) constructs a hexagonal tesselation of a planar region and aggregates points inside hexagonal bins.

The optional gridsize argument (default 100) gives the number of hexagons across the x-direction used in the hexagonal tiling. If specified as a list or a tuple of length two, gridsize fixes the number of hexagon in the x- and y-directions respectively in the tiling.
The optional parameter extent=(xmin, xmax, ymin, ymax) specifies rectangular region covered by the hexagonal tiling. In that case, xmin and xmax are the respective lower and upper limits for the variables on the x-axis and ymin and ymax are the respective lower and upper limits for the variables on the y-axis.
In this exercise, you'll use the same auto-mpg data as in the last exercise (again using arrays mpg and hp). This time, you'll use plt.hexbin() to visualize the two-dimensional histogram.

INSTRUCTIONS
100XP
Generate a two-dimensional histogram with plt.hexbin() to view the joint variation of the mpg and hp vectors.
Put hp along the horizontal axis and mpg along the vertical axis.
Specify a hexagonal tesselation with 15 hexagons across the x-direction and 12 hexagons across the y-direction using gridsize.
Specify the rectangular region covered with the optional extent argument: use hp from 40 to 235 and mpg from 8 to 48.
Add a color bar to the histogram.
'''
# Generate a 2d histogram with hexagonal bins
plt.hexbin(hp,mpg,gridsize=(15,12),extent=(40, 235, 8, 48))

           
# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()
