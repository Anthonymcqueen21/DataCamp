'''
Improving model weights

Hurray! You've just calculated the slopes you need. Now it's time to use those slopes to improve your model. If you add the slopes to your weights, you will move in the right direction. However, it's possible to move too far in that direction. So you will want to take a small step in that direction first, using a lower learning rate, and verify that the model is improving.

The weights have been pre-loaded as weights, the actual value of the target as target, and the input data as input_data. The predictions from the initial weights are stored as preds.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Set the learning rate to be 0.01 and calculate the error from the original predictions. This has been done for you.
Calculate the updated weights by subtracting the product of learning_rate and slope from weights.
Calculate the updated predictions by multiplying weights_updated with input_data and computing their sum.
Calculate the error for the new predictions. Store the result as error_updated.
Hit 'Submit Answer' to compare the updated error to the original!
'''
# Set the learning rate: learning_rate
learning_rate = 0.01

# Calculate the predictions: preds
preds = (weights * input_data).sum()

# Calculate the error: error
error = preds - target

# Calculate the slope: slope
slope = 2 * input_data * error

# Update the weights: weights_updated
weights_updated = weights - learning_rate * slope

# Get updated predictions: preds_updated
preds_updated = (weights_updated * input_data).sum()

# Calculate updated error: error_updated
error_updated = preds_updated - target

# Print the original error
print(error)

# Print the updated error
print(error_updated)
