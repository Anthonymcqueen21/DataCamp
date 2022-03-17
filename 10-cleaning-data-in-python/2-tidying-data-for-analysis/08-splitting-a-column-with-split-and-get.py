'''
Splitting a column with .split() and .get()

Another common way multiple variables are stored in columns is with a delimiter. You'll learn how
to deal with such cases in this exercise, using a dataset consisting of Ebola cases and death
counts by state and country. It has been pre-loaded into a DataFrame as ebola.

Print the columns of ebola in the IPython Shell using ebola.columns. Notice that the data has
column names such as Cases_Guinea and Deaths_Guinea. Here, the underscore _ serves as a delimiter
between the first part (cases or deaths), and the second part (country).

This time, you cannot directly slice the variable by position as in the previous exercise. You
now need to use Python's built-in string method called .split(). By default, this method will
split a string into parts separated by a space. However, in this case you want it to split by
an underscore. You can do this on Cases_Guinea, for example, using Cases_Guinea.split('_'),
which returns the list ['Cases', 'Guinea'].

The next challenge is to extract the first element of this list and assign it to a type variable,
and the second element of the list to a country variable. You can accomplish this by accessing
the str attribute of the column and using the .get() method to retrieve the 0 or 1 index, depending
on the part you want.

INSTRUCTIONS
100XP
-Melt ebola using 'Date' and 'Day' as the id_vars, 'type_country' as the var_name, and 'counts'
as the value_name.
-Create a column called 'str_split' by splitting the 'type_country' column of ebola_melt on '_'.
Note that you will first have to access the str attribute of type_country before you can use .split().
-Create a column called 'type' by using the .get() method to retrieve index 0 of the 'str_split'
column of ebola_melt.
-Create a column called 'country' by using the .get() method to retrieve index 1 of the 'str_split'
column of ebola_melt.
-Print the head of ebola. This has been done for you, so hit 'Submit Answer' to view the results!
'''
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())
