'''
Index values and names

Which one of the following index operations does not raise an error?

The sales DataFrame which you have seen in the videos of the previous chapter has been pre-loaded for you and is available for exploration in the IPython Shell.

       eggs  salt  spam
month                  
Jan      47  12.0    17
Feb     110  50.0    31
Mar     221  89.0    72
Apr      77  87.0    20
May     132   NaN    52
Jun     205  60.0    55
INSTRUCTIONS
50XP
Possible Answers
sales.index[0] = 'JAN'.
press 1

sales.index[0] = sales.index[0].upper().
press 2

sales.index = range(len(sales)).
'''
sales.index = range(len(sales))