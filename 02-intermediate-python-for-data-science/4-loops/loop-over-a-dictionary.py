'''
Loop over dictionary
100xp
In Python 3, you need the items() method to loop over a dictionary:

world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))
Remember the europe dictionary that contained the names of some European countries
as key and their capitals as corresponding value? Go ahead and write a loop to iterate over it!

Instructions
Write a for loop that goes through each key:value pair of europe. On each iteration,
"the capital of x is y" should be printed out, where x is the key and y is the value of the pair.
'''
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
          
# Iterate over europe
for k, v in europe.items():
    print("the capital of " + str(k) + " is " + str(v))
