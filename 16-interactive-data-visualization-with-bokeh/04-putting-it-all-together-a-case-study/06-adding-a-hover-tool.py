'''
Adding a hover tool

In this exercise, you'll practice adding a hover tool to drill down into data column values and display more detailed information about each scatter point.

After you're done, experiment with the hover tool and see how it displays the name of the country when your mouse hovers over a point!

The figure and slider have been created for you and are available in the workspace as plot and slider.

INSTRUCTIONS
0XP
Import HoverTool from bokeh.models.
Create a HoverTool object called hover with tooltips=[('Country', '@country')].
Add the HoverTool object you created to the plot using add_tools().
Create a row layout using widgetbox(slider) and plot.
Add the layout to the current document. This has already been done for you.
'''
# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool: hover
hover = HoverTool(tooltips=[('Country', '@country')])

# Add the HoverTool to the plot
plot.add_tools(hover)

# Create layout: layout
layout = row(widgetbox(slider), plot)

# Add layout to current document
curdoc().add_root(layout)
