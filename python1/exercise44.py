import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import webbrowser
from PyQt5.QtGui import QMovie

class TikTokSearchApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TikTok Search")
        layout = QVBoxLayout()

        label = QLabel("Enter a TikTok keyword:")
        layout.addWidget(label)

        self.search_input = QLineEdit()
        layout.addWidget(self.search_input)

        self.search_button = QPushButton("Search TikTok")
        layout.addWidget(self.search_button)
        self.search_button.clicked.connect(self.search_tiktok)

        # Create QLabel widget to display GIF
        self.gif_label = QLabel()
        self.gif = QMovie("loading.gif")
        self.gif_label.setMovie(self.gif)
        self.gif_label.setScaledContents(True)

        layout.addWidget(self.gif_label)

        # Initially, show the loading GIF
        self.gif_label.show()
        self.gif.start()

        self.setLayout(layout)

    def search_tiktok(self):
        keyword = self.search_input.text()

        # Hide the loading GIF
        self.gif_label.hide()
        self.gif.stop()

        # Check for invalid characters in the input
        invalid_chars = [',', '.', "'", '/', '[', ']', '{', '}', ';', '126534']  # Add more as needed
        if any(char in keyword for char in invalid_chars):
            self.show_gif("mistake.gif")
        else:
            tiktok_url = f"https://www.tiktok.com/tag/{keyword}"

            # Open the TikTok URL in the default web browser
            if webbrowser.open(tiktok_url):
                # Display the success GIF
                self.show_gif("success.gif")
            else:
                # Display the "mistake.gif" for other errors
                self.show_gif("mistake.gif")

    def show_gif(self, gif_file):
        self.gif = QMovie(gif_file)
        self.gif_label.setMovie(self.gif)
        self.gif_label.show()
        self.gif.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TikTokSearchApp()
    window.show()
    sys.exit(app.exec_())

        
        
        
        