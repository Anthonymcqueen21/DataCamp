'''
Synchronize two dropdowns

Here, you'll practice using a dropdown callback to update another dropdown's options. This will allow you to customize your applications even further and is a powerful addition to your toolbox.

Your job in this exercise is to create two dropdown select widgets and then define a callback such that one dropdown is used to update the other dropdown.

All modules necessary have been imported.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Create select1, the first dropdown select widget. Specify the parameters title, options, and value.
Create select2, the second dropdown select widget. Specify the parameters title, options, and value.
Inside the callback function, if select1 equals 'A', update the options of select2 to ['1', '2', '3'] and set its value to '1'.
If select1 does not equal 'A', update the options of select2 to ['100', '200', '300'] and set its value to '100'.
Attach the callback to the 'value' property of select1. This can be done using on_change() and passing in 'value' and callback.
'''
# Create two dropdown Select widgets: select1, select2
select1 = Select(title='First', options=['A', 'B'], value='A')
select2 = Select(title='Second', options=['1', '2', '3'], value='1')

# Define a callback function: callback
def callback(attr, old, new):
    # If select1 is 'A' 
    if select1.value == 'A':
        # Set select2 options to ['1', '2', '3']
        select2.options = ['1', '2', '3']

        # Set select2 value to '1'
        select2.value = '1'
    else:
        # Set select2 options to ['100', '200', '300']
        select2.options = ['100', '200', '300']

        # Set select2 value to '100'
        select2.value = '100'

# Attach the callback to the 'value' property of select1
select1.on_change('value', callback)

# Create layout and add to current document
layout = widgetbox(select1, select2)
curdoc().add_root(layout)
