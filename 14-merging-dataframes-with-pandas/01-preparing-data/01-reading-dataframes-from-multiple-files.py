'''
Reading DataFrames from multiple files

When data is spread among several files, you usually invoke pandas' read_csv() (or a similar data import function) multiple times to load the data into several DataFrames.

The data files for this example have been derived from a list of Olympic medals awarded between 1896 & 2008 compiled by the Guardian.

The column labels of each DataFrame are NOC, Country, & Total where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won (bronze, silver, or gold).

INSTRUCTIONS
100XP
Import pandas as pd.
Read the file 'Bronze.csv' into a DataFrame called bronze.
Read the file 'Silver.csv' into a DataFrame called silver.
Read the file 'Gold.csv' into a DataFrame called gold.
Print the first 5 rows of the DataFrame gold. This has been done for you, so hit 'Submit Answer' to see the results.
'''
# Import pandas
import pandas as pd

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())