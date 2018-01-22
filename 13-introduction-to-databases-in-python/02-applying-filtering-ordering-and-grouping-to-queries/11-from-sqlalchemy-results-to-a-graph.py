'''
From SQLAlchemy results to a Graph

We can also take advantage of pandas and Matplotlib to build figures of our data. Remember that data visualization is essential for both exploratory data analysis and communication of your data!

INSTRUCTIONS
100XP
Import matplotlib.pyplot as plt.
Create a DataFrame df using pd.DataFrame() on the provided results.
Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
Print the DataFrame df.
Use the plot.bar() method on df to create a bar plot of the results.
Display the plot with plt.show().
'''
# Import Pyplot as plt from matplotlib
import matplotlib.pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.barh()
plt.show()
