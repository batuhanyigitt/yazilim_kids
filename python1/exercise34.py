import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
sia = SentimentIntensityAnalyzer()
sentiments = {"Positive": 0, "Neutral": 0, "Negative": 0}
while True:
    user_input = input("bir seyler yaz (cikmak icin 'q' to quit): ").strip()

    if user_input.lower() == 'q':
        break

    sentiment_scores = sia.polarity_scores(user_input)

    if sentiment_scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    sentiments[sentiment] += 1
labels = sentiments.keys()
values = sentiments.values()
plt.bar(labels, values)
plt.title("Duygu durumu")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()