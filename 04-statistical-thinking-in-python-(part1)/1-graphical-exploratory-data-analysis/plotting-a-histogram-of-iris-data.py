'''
Plotting a histogram of iris data
100xp

For the exercises in this section, you will use a classic data set collected by
botanist Edward Anderson and made famous by Ronald Fisher, one of the most prolific
statisticians in history. Anderson carefully measured the anatomical properties of
samples of three different species of iris, Iris setosa, Iris versicolor, and Iris
virginica. The full data set is available as part of scikit-learn. Here, you will
work with his measurements of petal length.

Plot a histogram of the petal lengths of his 50 samples of Iris versicolor using
matplotlib/seaborn's default settings. Recall that to specify the default seaborn
style, you can use sns.set(), where sns is the alias that seaborn is imported as.

The subset of the data set containing the Iris versicolor petal lengths in units
of centimeters (cm) is stored in the NumPy array versicolor_petal_length.

In the video, Justin plotted the histograms by using the pandas library and indexing
the DataFrame to extract the desired column. Here, however, you only need to use the
provided NumPy array. Also, Justin assigned his plotting statements (except for plt.show())
to the dummy variable _. This is to prevent unnecessary output from being displayed.
It is not required for your solutions to these exercises, however it is good practice
to use it. Alternatively, if you are working in an interactive environment such as a
Jupyter notebook, you could use a ; after your plotting statements to achieve the same
effect. Justin prefers using _. Therefore, you will see it used in the solution code.

Instructions
-Import matplotlib.pyplot and seaborn as their usual aliases (plt and sns).
-Use seaborn to set the plotting defaults.
-Plot a histogram of the Iris versicolor petal lengths using plt.hist() and the
provided NumPy array versicolor_petal_length.
-Show the histogram using plt.show().
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

# Show histogram
plt.show()
