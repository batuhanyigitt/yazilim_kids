import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Generating synthetic data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predicting on the test data
y_pred = model.predict(X_test)

# Plot the data points
plt.scatter(X, y, color='blue', label='Data Points')

# Plot the regression line
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')

# Add labels and title
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression with Multiple Data Points')
plt.legend()

# Show the plot
plt.show()
