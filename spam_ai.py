import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from sklearn.model_selection import train_test_split

# Sample dataset (Spam and Non-Spam Messages)
data = {
    "message": [
        "Win a free iPhone now!", "Congratulations, you won a lottery!",
        "Hello, how are you?", "Let's meet for lunch.",
        "Get cheap loans today!", "This is a reminder for your appointment.",
        "Claim your prize before it's too late!", "Don't miss out on this offer!",
        "Hey, are you free this weekend?", "Call me when you have time."
    ],
    "label": [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]  # 1 = Spam, 0 = Not Spam
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df["message"], df["label"], test_size=0.2, random_state=42)

# Tokenize and pad sequences
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)

X_train_seq = pad_sequences(tokenizer.texts_to_sequences(X_train), maxlen=10, padding='post')
X_test_seq = pad_sequences(tokenizer.texts_to_sequences(X_test), maxlen=10, padding='post')

# Define LSTM Model
model = Sequential([
    Embedding(1000, 32, input_length=10),
    LSTM(32, return_sequences=True),
    LSTM(16),
    Dense(10, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train_seq, np.array(y_train), epochs=10, batch_size=2, validation_data=(X_test_seq, np.array(y_test)))

# Function to predict new messages
def predict_spam(message):
    seq = pad_sequences(tokenizer.texts_to_sequences([message]), maxlen=10, padding='post')
    prediction = model.predict(seq)[0][0]
    return "SPAM" if prediction > 0.5 else "NOT SPAM"

# 🔹 Test new messages
test_messages = [
    "Win a free vacation now!",
    "Hey, can we talk later?",
    "Exclusive offer just for you!",
    "Let's grab coffee tomorrow."
]

for msg in test_messages:
    print(f"Message: '{msg}' -> Prediction: {predict_spam(msg)}")
