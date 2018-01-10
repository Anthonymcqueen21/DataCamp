'''
Quantiles

In this exercise, you'll investigate the probabilities of life expectancy in countries around the world. This dataset contains life expectancy for persons born each year from 1800 to 2015. Since country names change or results are not reported, not every country has values. This dataset was obtained from Gapminder.

First, you will determine the number of countries reported in 2015. There are a total of 206 unique countries in the entire dataset. Then, you will compute the 5th and 95th percentiles of life expectancy over the entire dataset. Finally, you will make a box plot of life expectancy every 50 years from 1800 to 2000. Notice the large change in the distributions over this period.

The dataset has been pre-loaded into a DataFrame called df.

INSTRUCTIONS
100XP
-Print the number of countries reported in 2015. To do this, use the .count() method on the '2015' column of df.
-Print the 5th and 95th percentiles of df. To do this, use the .quantile() method with the list [0.05, 0.95].
-Generate a box plot using the list of columns provided in years. This has already been done for you, so click on 'Submit Answer' to view the result!
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../_datasets/life_expectancy_at_birth.csv')

# Print the number of countries reported in 2015
print(df['2015'].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05, 0.95]))

# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()
