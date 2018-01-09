'''
mport package
100xp
As a data scientist, some notions of geometry never hurt. Let's refresh some of the basics.

For a fancy clustering algorithm, you want to find the circumference, C
, and area, A
, of a circle. When the radius of the circle is r, you can calculate C
 and A
 as:

C=2πr
A=πr2
To use the constant pi, you'll need the math package. A variable r is already coded in the script. Fill in the code to calculate C and A and see how the print() functions create some nice printouts.

Instructions
Import the math package. Now you can access the constant pi with math.pi.
Calculate the circumference of the circle and store it in C.
Calculate the area of the circle and store it in A.
'''

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * (r**2)

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))