'''
Writing an iterator to load data in chunks (3)
100xp

You're getting used to reading and processing data in chunks by now. Let's push your skills a
little further by adding a column to a DataFrame.

In this exercise, you will be using a list comprehension to create the values for a new column
'Total Urban Population' from the list of tuples that you generated earlier. Recall from the
previous exercise that the first and second elements of each tuple consist of, respectively,
values from the columns 'Total Population' and 'Urban population (% of total)'. The values in
this new column 'Total Urban Population', therefore, are the product of the first and second
element in each tuple. Furthermore, because the 2nd element is a percentage, you need to divide
the entire result by 100, or alternatively, multiply it by 0.01.

You will also plot the data from this new column to create a visualization of the urban
population data.

You're going to use the data from 'ind_pop_data.csv', available in your current directory.
The packages pandas and matplotlib.pyplot have been imported as pd and plt respectively for your use.

Instructions
-Use pd.read_csv() to read in the file 'ind_pop_data.csv' in chunks of size 1000. Assign the
result to urb_pop_reader.
-Write a list comprehension to generate a list of values from pops_list for the new column
'Total Urban Population'. Use tup as the iterator variable. The output expression should be the
product of the first and second element in each tuple in pops_list. Because the 2nd element is a
percentage, you also need to either multiply the result by 0.01 or divide it by 100. In addition,
note that the column 'Total Urban Population' should only be able to take on integer values.
To ensure this, make sure you cast the output expression to an integer with int().
-Create a scatter plot where the x-axis are values from the 'Year' column and the y-axis are values
from the 'Total Urban Population' column.
'''
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], 
            df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()
