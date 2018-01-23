'''
Modifying colormaps

When displaying a 2-D array with plt.imshow() or plt.pcolor(), the values of the array are mapped to a corresponding color. The set of colors used is determined by a colormap which smoothly maps values to colors, making it easy to understand the structure of the data at a glance.

It is often useful to change the colormap from the default 'jet' colormap used by matplotlib. A good colormap is visually pleasing and conveys the structure of the data faithfully and in a way that makes sense for the application.

Some matplotlib colormaps have unique names such as 'jet', 'coolwarm', 'magma' and 'viridis'.
Others have a naming scheme based on overall color such as 'Greens', 'Blues', 'Reds', and 'Purples'.
Another four colormaps are based on the seasons, namely 'summer', 'autumn', 'winter' and 'spring'.
You can insert the option cmap=<name> into most matplotlib functions to change the color map of the resulting plot.
In this exercise, you will explore four different colormaps together using plt.subplot(). You will use a pregenerated array Z and a meshgrid X, Y to generate the same filled contour plot with four different color maps. Be sure to also add a color bar to each filled contour plot with plt.colorbar().

INSTRUCTIONS
100XP
Modify the call to plt.contourf() so the filled contours in the top left subplot use the 'viridis' colormap.
Modify the call to plt.contourf() so the filled contours in the top right subplot use the 'gray' colormap.
Modify the call to plt.contourf() so the filled contours in the bottom left subplot use the 'autumn' colormap.
Modify the call to plt.contourf() so the filled contours in the bottom right subplot use the 'winter' colormap.
'''
# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2,2,1)
plt.contourf(X,Y,Z,20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')

# Create a filled contour plot with a color map of 'gray'
plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')

# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2,2,3)
plt.contourf(X,Y,Z,20, cmap='autumn')
plt.colorbar()
plt.title('Autumn')

# Create a filled contour plot with a color map of 'winter'
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20, cmap='winter')
plt.colorbar()
plt.title('Winter')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()
