'''
Beginning with just a plot

Let's get started on the Gapminder app. Your job is to make the ColumnDataSource object, prepare the plot, and add circles for Life expectancy vs Fertility. You'll also set x and y ranges for the axes.

As in the previous chapter, the DataCamp environment executes the bokeh serve command to run the app for you. When you hit 'Submit Answer', you'll see in the IPython Shell that bokeh serve script.py gets called to run the app. This is something to keep in mind when you are creating your own interactive visualizations outside of the DataCamp environment.

INSTRUCTIONS
100XP
Make a ColumnDataSource object called source with 'x', 'y', 'country', 'pop' and 'region' keys. The Pandas selections are provided for you.
Save the minimum and maximum values of the life expectancy column data.life as ymin and ymax. As a guide, you can refer to the way we saved the minimum and maximum values of the fertility column data.fertility as xmin and xmax.
Create a plot called plot() by specifying the title, setting plot_height to 400, plot_width to 700, and adding the x_range and y_range parameters.
Add circle glyphs to the plot. Specify an fill_alpha of 0.8 and source=source.
'''
# Import the necessary modules
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x'       : data.loc[1970].fertility,
    'y'       : data.loc[1970].life,
    'country'      : data.loc[1970].Country,
    'pop'      : (data.loc[1970].population / 20000000) + 2,
    'region'      : data.loc[1970].region,
})

# Save the minimum and maximum values of the fertility column: xmin, xmax
xmin, xmax = min(data.fertility), max(data.fertility)

# Save the minimum and maximum values of the life expectancy column: ymin, ymax
ymin, ymax = min(data.life), max(data.life)

# Create the figure: plot
plot = figure(title='Gapminder Data for 1970', plot_height=400, plot_width=700, x_range=(xmin, xmax), y_range=(ymin, ymax))

# Add circle glyphs to the plot
plot.circle(x='x', y='y', fill_alpha=0.8, source=source)

# Set the x-axis label
plot.xaxis.axis_label ='Fertility (children per woman)'

# Set the y-axis label
plot.yaxis.axis_label = 'Life Expectancy (years)'

# Add the plot to the current document and add a title
curdoc().add_root(plot)
curdoc().title = 'Gapminder'
