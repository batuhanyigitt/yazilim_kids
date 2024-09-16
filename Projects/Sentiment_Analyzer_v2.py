import sys
from textblob import TextBlob
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QTextEdit, QMessageBox

class SentimentAnalysisApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sentiment Analysis")
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.analyze_button = QPushButton("Analyze Sentiment")
        self.analyze_button.clicked.connect(self.analyze_sentiment)
        layout.addWidget(self.analyze_button)

        self.central_widget.setLayout(layout)

    def analyze_sentiment(self):
        text = self.text_edit.toPlainText()
        if text.strip():
            blob = TextBlob(text)
            sentiment = blob.sentiment.polarity

            if sentiment > 0:
                sentiment_label = "Positive"
            elif sentiment < 0:
                sentiment_label = "Negative"
            else:
                sentiment_label = "Neutral"

            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle("Sentiment Analysis Result")
            message_box.setText(f"Sentiment: {sentiment_label}")
            message_box.exec_()
        else:
            QMessageBox.warning(self, "Warning", "Please enter some text to analyze.", QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SentimentAnalysisApp()
    window.show()
    sys.exit(app.exec_())