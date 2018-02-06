'''
Adding dropdowns to the app

As a final step in enhancing your application, in this exercise you'll add dropdowns for interactively selecting different data features. In combination with the hover tool you added in the previous exercise, as well as the slider to change the year, you'll have a powerful app that allows you to interactively and quickly extract some great insights from the dataset!

All necessary modules have been imported, and the previous code you wrote is taken care off. In the provided sample code, the dropdown for selecting features on the x-axis has been added for you. Using this as a reference, your job in this final exercise is to add a dropdown menu for selecting features on the y-axis.

Take a moment, after you are done, to enjoy exploring the visualization by experimenting with the hover tools, sliders, and dropdown menus that you have learned how to implement in this course.

INSTRUCTIONS
0XP
Inside the update_plot() callback function, read in the current value of the y dropdown, y_select.
Use plot.yaxis.axis_label to label the y-axis as y.
Set the start and end range of the y-axis of plot.
Specify the parameters of the y_select dropdown widget: options, value, and title. The default value should be 'life'.
Attach the callback to the 'value' property of y_select. This can be done using on_change() and passing in 'value' and update_plot.
'''
# Define the callback: update_plot
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = x_select.value
    y = y_select.value
    # Label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    # Set new_data
    new_data = {
        'x'       : data.loc[yr][x],
        'y'       : data.loc[yr][y],
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes
    plot.x_range.start = min(data[x])
    plot.x_range.end = max(data[x])
    plot.y_range.start = min(data[y])
    plot.y_range.end = max(data[y])

    # Add title to plot
    plot.title.text = 'Gapminder data for %d' % yr

# Create a dropdown slider widget: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Create a dropdown Select widget for the x data: x_select
x_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='fertility',
    title='x-axis data'
)

# Attach the update_plot callback to the 'value' property of x_select
x_select.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='life',
    title='y-axis data'
)

# Attach the update_plot callback to the 'value' property of y_select
y_select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select), plot)
curdoc().add_root(layout)