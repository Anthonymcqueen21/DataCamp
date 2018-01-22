'''
Loading a CSV into a Table

You've done a great job so far at inserting data into tables! You're now going to learn how to load the contents of a CSV file into a table.

We have used the csv module to set up a csv_reader, which is just a reader object that can iterate over the lines in a given CSV file - in this case, a census CSV file. Using the enumerate() function, you can loop over the csv_reader to handle the results one at a time. Here, for example, the first line it would return is:

0 ['Illinois', 'M', '0', '89600', '95012']

0 is the idx - or line number - while ['Illinois', 'M', '0', '89600', '95012'] is the row, corresponding to the column names 'state' , 'sex', 'age', 'pop2000 'and 'pop2008'. 'Illinois' can be accessed with row[0], 'M' with row[1], and so on. You can create a dictionary containing this information where the keys are the column names and the values are the entries in each line. Then, by appending this dictionary to a list, you can combine it with an insert statement to load it all into a table!

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Create a statement for bulk insert into the census table. To do this, just use insert() and census.
Create an empty list called values_list and a variable called total_rowcount that is set to 0.
Within the for loop:
Complete the data dictionary by filling in the values for each of the keys. The values are contained in row. row[0] represents the value for 'state', row[1] represents the value for 'sex', and so on.
Append data to values_list.
If 51 cleanly divides into the current idx:
Execute stmt with the values_list and save it as results.
Hit 'Submit Answer' to print total_rowcount when done with all the records.
'''
# Create a insert statement for census: stmt
stmt = insert(census)

# Create an empty list and zeroed row count: values_list, total_rowcount
values_list = []
total_rowcount = 0

# Enumerate the rows of csv_reader
for idx, row in enumerate(csv_reader):
    #create data and append to values_list
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3],'pop2008': row[4]}
    values_list.append(data)

    # Check to see if divisible by 51
    if idx % 51 == 0:
        results = connection.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []

# Print total rowcount
print(total_rowcount)
