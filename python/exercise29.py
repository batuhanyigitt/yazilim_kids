import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt 

sia = SentimentIntensityAnalyzer()

texts = [
    "I love this movie",
    "I hate this movie",
    "This movie is okay, but it could be better",
    "I'm feeling great today"
]

sentiments = {"Positive": 0, "Neutral": 0, "Negative": 0}

for text in texts:
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_score['compound'] <= 0.05:
        sentiment = 'Negative'
    else: 
        sentiment = 'Neutral'
        
labels = sentiments.keys()
values = sentiments.values()

plt.bar(labels, values)
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()