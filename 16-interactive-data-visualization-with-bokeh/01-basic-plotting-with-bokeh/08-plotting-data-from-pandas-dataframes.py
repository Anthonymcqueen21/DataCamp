'''
Plotting data from Pandas DataFrames

You can create Bokeh plots from Pandas DataFrames by passing column selections to the glyph functions.

Bokeh can plot floating point numbers, integers, and datetime data types. In this example, you will read a CSV file containing information on 392 automobiles manufactured in the US, Europe and Asia from 1970 to 1982.

The CSV file is provided for you as 'auto.csv'.

Your job is to plot miles-per-gallon (mpg) vs horsepower (hp) by passing Pandas column selections into the p.circle() function. Additionally, each glyph will be colored according to values in the color column.

INSTRUCTIONS
100XP
Import pandas as pd.
Use the read_csv() function of pandas to read in 'auto.csv' and store it in the DataFrame df.
Import figure from bokeh.plotting.
Use the figure() function to create a figure p with the x-axis labeled 'HP' and the y-axis labeled 'MPG'.
Plot mpg (on the y-axis) vs hp (on the x-axis) by color using p.circle(). Note that the x-axis should be specified before the y-axis inside p.circle(). You will need to use Pandas DataFrame indexing to pass in the columns. For example, to access the color column, you can use df['color'], and then pass it in as an argument to the color parameter of p.circle(). Also specify a size of 10.
'''
# Import pandas as pd
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('auto.csv')

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create the figure: p
p = figure(x_axis_label='HP', y_axis_label='MPG')

# Plot mpg vs hp by color
p.circle(df['hp'], df['mpg'], color=df['color'], size=10)

# Specify the name of the output file and show the result
output_file('auto-df.html')
show(p)
