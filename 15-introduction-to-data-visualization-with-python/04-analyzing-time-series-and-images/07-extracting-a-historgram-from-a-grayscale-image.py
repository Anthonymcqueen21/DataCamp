'''
Extracting a histogram from a grayscale image

For grayscale images, various image processing algorithms use an image histogram. Recall that an image is a two-dimensional array of numerical intensities. An image histogram, then, is computed by counting the occurences of distinct pixel intensities over all the pixels in the image.

For this exercise, you will load an unequalized low contrast image of Hawkes Bay, New Zealand (originally by Phillip Capper, modified by User:Konstable, via Wikimedia Commons, CC BY 2.0). You will plot the image and use the pixel intensity values to plot a normalized histogram of pixel intensities.

INSTRUCTIONS
100XP
Load data from the file '640px-Unequalized_Hawkes_Bay_NZ.jpg' into an array.
Display image with a color map of 'gray' in the top subplot.
Flatten image into a 1-D array using the .flatten() method.
Display a histogram of pixels in the bottom subplot.
Use histogram options bins=64, range=(0,256), and normed=True to control numerical binning and the vertical scale.
Use plotting options color='red' and alpha=0.4 to tailor the color and transparency.
'''
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, color='red', alpha=0.4, range=(0, 256), normed=True)

# Display the plot
plt.show()
