'''
Dictionary Manipulation (2)
100xp
Somebody thought it would be funny to mess with your accurately generated dictionary.
An adapted version of the europe dictionary is available in the script on the right.

Can you clean up? Do not do this by adapting the definition of europe, but by adding
Python commands to the script to update and remove key:value pairs.

Instructions
-The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
-Australia is not in Europe, Austria is! Remove they key 'australia' from europe.
-Print out europe to see if your cleaning work paid off.
'''
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)
