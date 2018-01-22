'''
SQLAlchemy ResultsProxy and Pandas Dataframes

We can feed a ResultProxy directly into a pandas DataFrame, which is the workhorse of many Data Scientists in PythonLand. Jason demonstrated this in the video. In this exercise, you'll follow exactly the same approach to convert a ResultProxy into a DataFrame.

INSTRUCTIONS
100XP
Import pandas as pd.
Create a DataFrame df using pd.DataFrame() on the ResultProxy results.
Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
Print the DataFrame.
'''
# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)
