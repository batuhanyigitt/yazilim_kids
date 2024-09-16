import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# Define some example sentences
sentences = [
    "I love this product, it's amazing!",
    "This movie is really great, I enjoyed it a lot.",
    "The food at this restaurant is delicious.",
    "I hate waiting in long queues, it's frustrating.",
    "This service is terrible, I wouldn't recommend it to anyone.",
    "The weather today is just okay, nothing special.",
    "I feel indifferent about this book, neither good nor bad."
]

# Assign sentiment labels
sentiment_labels = ['positive', 'positive', 'positive',
                    'negative', 'negative', 'neutral', 'neutral']

# Create a DataFrame
data = pd.DataFrame({'text': sentences, 'sentiment': sentiment_labels})

# Shuffle the data
data = data.sample(frac=1).reset_index(drop=True)

# Save the data to a CSV file
data.to_csv('sentiment_data.csv', index=False)


# Load Dataset
data = pd.read_csv('sentiment_data.csv')

# Preprocessing
tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(data['text'])
sequences = tokenizer.texts_to_sequences(data['text'])
padded_sequences = pad_sequences(sequences, maxlen=100, padding='post', truncating='post')
labels = pd.get_dummies(data['sentiment']).values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

# Build Model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=10000, output_dim=16, input_length=100),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train Model
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluate Model
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

# Make Predictions
new_texts = ["I love this product!", "This is terrible."]
new_sequences = tokenizer.texts_to_sequences(new_texts)
new_padded_sequences = pad_sequences(new_sequences, maxlen=100, padding='post', truncating='post')

predictions = model.predict(new_padded_sequences)
print(predictions)
