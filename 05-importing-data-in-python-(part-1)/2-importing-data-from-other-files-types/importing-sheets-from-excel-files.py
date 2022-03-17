'''
Importing sheets from Excel files
100xp

In the previous exercises, you saw that the Excel file contains two sheets,
'2002' and '2004'. The next step is to import these.

In this exercise, you'll learn how to import any given sheet of your loaded
.xslx file as a DataFrame. You'll be able to do so by specifying either the
sheet's name or its index.

The spreadsheet 'battledeath.xlsx' is already loaded as xl.

Instructions
-Load the sheet '2004' into the DataFrame df1 using its name as a string.
-Print the head of df1 to the shell.
-Load the sheet 2002 into the DataFrame df2 using its index.
-Print the head of df2 to the shell.
'''
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = '../_datasets/battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())
