import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

# Download NLTK data online
nltk.download('vader_lexicon')

class SentimentAnalysisApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.sia = SentimentIntensityAnalyzer()

        self.texts = [
            "I love this movie",
            "I hate this movie",
            "This movie is okay, but it could be better",
            "I'm feeling great today"
        ]

        self.sentiments = {"Positive": 0, "Neutral": 0, "Negative": 0}

        for text in self.texts:
            sentiment_score = self.sia.polarity_scores(text)
            if sentiment_score['compound'] >= 0.05:
                sentiment = 'Positive'
            elif sentiment_score['compound'] <= -0.05:
                sentiment = 'Negative'
            else:
                sentiment = 'Neutral'
            self.sentiments[sentiment] += 1

        self.display_sentiment_images()
        self.display_sentiment_chart()

        layout = QVBoxLayout()
        layout.addWidget(self.sentiment_images_label)
        layout.addWidget(self.sentiment_chart_label)
        self.setLayout(layout)

        self.setWindowTitle("Sentiment Analysis App")

    def display_sentiment_images(self):
        self.sentiment_images_label = QLabel()

        positive_image = QPixmap("positive.png")  # Replace with your positive image URL
        neutral_image = QPixmap("neutral.png")    # Replace with your neutral image URL
        negative_image = QPixmap("negative.png")  # Replace with your negative image URL

        images = {
            "Positive": positive_image,
            "Neutral": neutral_image,
            "Negative": negative_image
        }

        for sentiment, image in images.items():
            self.sentiment_images_label.setPixmap(image)
            self.sentiment_images_label.setAlignment(Qt.AlignCenter)
            self.sentiment_images_label.setText(sentiment)
            self.sentiment_images_label.show()
            QApplication.processEvents()

    def display_sentiment_chart(self):
        labels = self.sentiments.keys()
        values = self.sentiments.values()

        plt.bar(labels, values, color=['green', 'yellow', 'red'])
        plt.title("Sentiment Analysis")
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.savefig("sentiment_chart.png")  # Save the chart as an image
        plt.close()

        self.sentiment_chart_label = QLabel()
        sentiment_chart_image = QPixmap("sentiment_chart.png")
        self.sentiment_chart_label.setPixmap(sentiment_chart_image)
        self.sentiment_chart_label.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sentiment_app = SentimentAnalysisApp()
    sentiment_app.show()
    sys.exit(app.exec_())
