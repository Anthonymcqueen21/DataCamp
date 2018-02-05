'''
Hover glyphs

Now let's practice using and customizing the hover tool.

In this exercise, you're going to plot the blood glucose levels for an unknown patient. The blood glucose levels were recorded every 5 minutes on October 7th starting at 3 minutes past midnight.

The date and time of each measurement are provided to you as x and the blood glucose levels in mg/dL are provided as y.

A bokeh figure is also provided in the workspace as p.

Your job is to add a circle glyph that will appear red when the mouse is hovered near the data points. You will also add a customized hover tool object to the plot.

When you're done, play around with the hover tool you just created! Notice how the points where your mouse hovers over turn red.

INSTRUCTIONS
100XP
Import HoverTool from bokeh.models.
Add a circle glyph to the existing figure p for x and y with a size of 10, fill_color of 'grey', alpha of 0.1, line_color of None, hover_fill_color of 'firebrick', hover_alpha of 0.5, and hover_line_color of 'white'.
Use the HoverTool() function to create a HoverTool called hover with tooltips=None and mode='vline'.
Add the HoverTool hover to the figure p using the p.add_tools() function.
'''
# import the HoverTool
from bokeh.models import HoverTool

# Add circle glyphs to figure p
p.circle(x, y, size=10,
         fill_color='grey', alpha=0.1, line_color=None,
         hover_fill_color='firebrick', hover_alpha=0.5,
         hover_line_color='white')

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode='vline')

# Add the hover tool to the figure p
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('hover_glyph.html')
show(p)
