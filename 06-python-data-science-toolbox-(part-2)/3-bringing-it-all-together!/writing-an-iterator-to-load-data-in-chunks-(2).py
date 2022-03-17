'''
Writing an iterator to load data in chunks (2)
100xp

In the previous exercise, you used read_csv() to read in DataFrame chunks from a large dataset.
In this exercise, you will read in a file using a bigger DataFrame chunk size and then process
the data from the first chunk.

To process the data, you will create another DataFrame composed of only the rows from a specific
country. You will then zip together two of the columns from the new DataFrame, 'Total Population' 
and 'Urban population (% of total)'. Finally, you will create a list of tuples from the zip object,
where each tuple is composed of a value from each of the two columns mentioned.

You're going to use the data from 'ind_pop_data.csv', available in your current directory. Pandas
has been imported as pd.

Instructions
-Use pd.read_csv() to read in the file in 'ind_pop_data.csv' in chunks of size 1000. Assign the
result to urb_pop_reader.
-Get the first DataFrame chunk from the iterable urb_pop_reader and assign this to df_urb_pop.
-Select only the rows of df_urb_pop that have a 'CountryCode' of 'CEB'. To do this, compare whether
df_urb_pop['CountryCode'] is equal to 'CEB' within the square brackets in df_urb_pop[____].
-Using zip(), zip together the 'Total Population' and 'Urban population (% of total)' columns of
df_pop_ceb. Assign the resulting zip object to pops.
'''
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], 
            df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)
