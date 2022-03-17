'''
Button widgets

It's time to practice adding buttons to your interactive visualizations. Your job in this exercise is to create a button and use its on_click() method to update a plot.

All necessary modules have been imported for you. In addition, the ColumnDataSource with data x and y as well as the figure have been created for you and are available in the workspace as source and plot.

When you're done, be sure to interact with the button you just added to your plot, and notice how it updates the data!

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Create a button called button using the function Button() with the label 'Update Data'.
Define an update callback update() with no arguments.
Compute new y values using the code provided.
Update the ColumnDataSource data dictionary source.data with the new y value.
Add the update callback to the button using on_click().
'''
# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():

    # Compute new y values: y
    y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x': x, 'y': y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)
