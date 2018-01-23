'''
Grouping linear regressions by hue

Often it is useful to compare and contrast trends between different groups. Seaborn makes it possible to apply linear regressions separately for subsets of the data by applying a groupby operation. Using the hue argument, you can specify a categorical variable by which to group data observations. The distinct groups of points are used to produce distinct regressions with different hues in the plot.

In the automobile dataset - which has been pre-loaded here as auto - you can view the relationship between weight ('weight') and horsepower ('hp') of the cars and group them by their origin ('origin'), giving you a quick visual indication how the relationship differs by continent.

INSTRUCTIONS
100XP
Plot a linear regression between 'weight' and 'hp' grouped by 'origin'.
Use the keyword argument hue to group rows with the categorical column 'origin'.
Use the keyword argument palette to specify the 'Set1' palette for coloring the distinct groups.
'''
# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(data=auto, x='weight', y='hp', hue='origin', palette='Set1')

# Display the plot
plt.show()
