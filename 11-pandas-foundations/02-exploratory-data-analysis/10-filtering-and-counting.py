'''
Filtering and counting

How many automobiles were manufactured in Asia in the automobile dataset? The DataFrame has been provided for you as df. Use filtering and the .count() member method to determine the number of rows where the 'origin' column has the value 'Asia'.

As an example, you can extract the rows that contain 'US' as the country of origin using df[df['origin'] == 'US'].

INSTRUCTIONS
50XP
Possible Answers
68
press 1

79
press 2

245
press 3

392
press 4
'''
import pandas as pd

df = pd.read_csv('../_datasets/auto-mpg.csv')

print(df[df['origin'] == 'Asia'].count())


79