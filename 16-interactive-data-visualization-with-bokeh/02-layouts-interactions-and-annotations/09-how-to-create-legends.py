'''
How to create legends

Legends can be added to any glyph by using the legend keyword argument.

In this exercise, you will plot two circle glyphs for female literacy vs fertility in Africa and Latin America.

Two ColumnDataSources called latin_america and africa have been provided.

Your job is to plot two circle glyphs for these two objects with fertility on the x axis and female_literacy on the y axis and add the legend values. The figure p has been provided for you.

INSTRUCTIONS
100XP
Add a red circle glyph to the figure p using the latin_america ColumnDataSource. Specify a size of 10 and legend of Latin America.
Add a blue circle glyph to the figure p using the africa ColumnDataSource. Specify a size of 10 and legend of Africa.
'''
# Add the first circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=latin_america, size=10, color='red', legend='Latin America')

# Add the second circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=africa, size=10, color='blue', legend='Africa')

# Specify the name of the output_file and show the result
output_file('fert_lit_groups.html')
show(p)
