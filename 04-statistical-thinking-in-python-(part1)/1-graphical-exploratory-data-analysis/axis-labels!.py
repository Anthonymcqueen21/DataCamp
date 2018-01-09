'''
Axis labels!
100xp
In the last exercise, you made a nice histogram of petal lengths of Iris versicolor,
but you didn't label the axes! That's ok; it's not your fault since we didn't ask you to.
Now, add axis labels to the plot using plt.xlabel() and plt.ylabel(). Don't forget to add
units and assign both statements to _. The packages matplotlib.pyplot and seaborn are already
imported with their standard aliases. This will be the case in what follows, unless specified
otherwise.

Instructions
Label the axes. Don't forget that you should always include units in your axis labels. Your
y-axis label is just 'count'. Your x
-axis label is 'petal length (cm)'. The units are essential!
Display the plot constructed in the above steps using plt.show().
'''
# Import plotting modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

versicolor_petal_length = np.array([ 4.7,  4.5,  4.9,  4. ,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
        4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,
        4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9,
        5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3,
        4.2,  4.2,  4.2,  4.3,  3. ,  4.1])

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()