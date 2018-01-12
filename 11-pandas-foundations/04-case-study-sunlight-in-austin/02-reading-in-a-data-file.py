'''
Reading in a data file

Now that you have identified the method to use to read the data, let's try to read one file. The problem with real data such as this is that the files are almost never formatted in a convenient way. In this exercise, there are several problems to overcome in reading the file. First, there is no header, and thus the columns don't have labels. There is also no obvious index column, since none of the data columns contain a full date or time.

Your job is to read the file into a DataFrame using the default arguments. After inspecting it, you will re-read the file specifying that there are no headers supplied.

The CSV file has been provided for you as 'data.csv'.

INSTRUCTIONS
100XP
-Import pandas as pd.
-Read the file 'data.csv' into a DataFrame called df.
-Print the output of df.head(). This has been done for you. Notice the formatting problems in df.
-Re-read the data using specifying the keyword argument header=None and assign it to df_headers.
-Print the output of df_headers.head(). This has already been done for you. Hit 'Submit Answer' and see how this resolves the formatting issues.
'''
# Import pandas
import pandas as pd

# Read in the data file: df
df = pd.read_csv('data.csv')

# Print the output of df.head()
print(df.head())

# Read in the data file with header=None: df_headers
df_headers = pd.read_csv('data.csv', header=None)
