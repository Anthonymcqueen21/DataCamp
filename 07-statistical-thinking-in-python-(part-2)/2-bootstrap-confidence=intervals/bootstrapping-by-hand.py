'''
Bootstrapping by hand

To help you gain intuition about how bootstrapping works, imagine you have a data set that has only
three points, [-1, 0, 1]. How many unique bootstrap samples can be drawn (e.g., [-1, 0, 1] and [1, 0, -1]
are unique), and what is the maximum mean you can get from a bootstrap sample? It might be useful to
jot down the samples on a piece of paper.

(These are too few data to get meaningful results from bootstrap procedures, but this example is useful
for intuition.)

INSTRUCTIONS
50XP
Possible Answers
-There are 3 unique samples, and the maximum mean is 0.
-There are 10 unique samples, and the maximum mean is 0.
-There are 10 unique samples, and the maximum mean is 1.
-There are 27 unique samples, and the maximum mean is 0.
-There are 27 unique samples, and the maximum mean is 1.
'''
# There are 27 unique samples, and the maximum mean is 1.