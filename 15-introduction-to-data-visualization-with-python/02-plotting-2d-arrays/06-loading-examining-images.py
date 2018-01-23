'''
Loading, examining images

Color images such as photographs contain the intensity of the red, green and blue color channels.

To read an image from file, use plt.imread() by passing the path to a file, such as a PNG or JPG file.
The color image can be plotted as usual using plt.imshow().
The resulting image loaded is a NumPy array of three dimensions. The array typically has dimensions M×N×3
M
×
N
×
3
, where M×N
M
×
N
 is the dimensions of the image. The third dimensions are referred to as color channels (typically red, green, and blue).
The color channels can be extracted by Numpy array slicing.
In this exercise, you will load & display an image of an astronaut (by NASA (Public domain), via Wikimedia Commons). You will also examine its attributes to understand how color images are represented.

INSTRUCTIONS
0XP
Load the file '480px-Astronaut-EVA.jpg' into an array.
Print the shape of the img array. How wide and tall do you expect the image to be?
Prepare img for display using plt.imshow().
Turn off the axes using plt.axis('off').
'''
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Display the image
plt.imshow(img)

# Hide the axes
plt.axis('off')
plt.show()