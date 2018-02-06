'''
Button styles

You can also get really creative with your Button widgets.

In this exercise, you'll practice using CheckboxGroup, RadioGroup, and Toggle to add multiple Button widgets with different styles.

curdoc and widgetbox have already been imported for you.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import CheckboxGroup, RadioGroup, Toggle from bokeh.models.
Add a Toggle called toggle using the Toggle() function with button_type 'success' and label 'Toggle button'.
Add a CheckboxGroup called checkbox using the CheckboxGroup() function with labels=['Option 1', 'Option 2', 'Option 3'].
Add a RadioGroup called radio using the RadioGroup() function with labels=['Option 1', 'Option 2', 'Option 3'].
Add the widgetbox containing the Toggle toggle, CheckboxGroup checkbox, and RadioGroup radio to the current document.
'''
# Import CheckboxGroup, RadioGroup, Toggle from bokeh.models
from bokeh.models import CheckboxGroup, RadioGroup, Toggle

# Add a Toggle: toggle
toggle = Toggle(label='Toggle button',button_type='success')

# Add a CheckboxGroup: checkbox
checkbox = CheckboxGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add a RadioGroup: radio
radio = RadioGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add widgetbox(toggle, checkbox, radio) to the current document
curdoc().add_root(widgetbox(toggle, checkbox, radio))