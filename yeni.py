import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
# Load the MNIST dataset
print("Loading dataset...")
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist.data, mnist.target

# Preprocess the data
X = X / 255.0  # Normalize pixel values
y = y.astype(int)  # Convert labels to integers
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train a Logistic Regression model
print("Training the model...")
model = LogisticRegression(solver='saga', multi_class='multinomial', max_iter=1000)
model.fit(X_train, y_train)

# Evaluate the model
print("Evaluating the model...")
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Test with a random digit
def predict_random_digit():
    idx = np.random.randint(0, len(X_test))
    digit_image = X_test[idx].reshape(28, 28)
    
    plt.imshow(digit_image, cmap='gray')
    plt.title("Input Image")
    plt.show()
    
    prediction = model.predict([X_test[idx]])[0]
    print(f"Model Prediction: {prediction}")

# Test the model with a random digit
predict_random_digit()
