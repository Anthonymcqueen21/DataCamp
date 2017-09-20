'''
A brief introduction to tuples
100xp

Alongside learning about functions, you've also learned about tuples!
Here, you will practice what you've learned about tuples: how to construct, unpack,
and access tuple elements. Recall how Hugo unpacked the tuple even_nums in the video:

a, b, c = even_nums

A three-element tuple named nums has been preloaded for this exercise.
Before completing the script, perform the following:

-Print out the value of nums in the IPython shell. Note the elements in the tuple.
-In the IPython shell, try to change the first element of nums to the value 2 by doing an assignment:
nums[0] = 2. What happens?

Instructions
-Unpack nums to the variables num1, num2, and num3.
-Construct a new tuple, even_nums composed of the same elements in nums, but with the 1st element replaced with the value, 2.
'''
nums = (3, 4, 6)

# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums

# Construct even_nums
even_nums = (2, num2, num3)
