import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
import random
import string

class PasswordGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Guessing Game')
        self.setGeometry(100, 100, 400, 250)

        self.label_instruction = QLabel('Enter your guess:', self)
        self.label_instruction.move(20, 30)

        self.textbox_guess = QLineEdit(self)
        self.textbox_guess.move(20, 60)

        self.button_guess = QPushButton('Guess', self)
        self.button_guess.move(20, 100)
        self.button_guess.clicked.connect(self.check_guess)

        self.label_password = QLabel(f'Correct Password: {self.generate_password()}', self)
        self.label_password.move(20, 140)

        self.attempts = 0
        self.max_attempts = 3

    def generate_password(self, length=12, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        characters = ''
        if include_lowercase:
            characters += lowercase_letters
        if include_uppercase:
            characters += uppercase_letters
        if include_digits:
            characters += digits
        if include_symbols:
            characters += symbols

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def check_guess(self):
        guess = self.textbox_guess.text()
        if guess == self.label_password.text().split(": ")[1]:
            QMessageBox.information(self, 'Congratulations!', 'You guessed the password correctly!')
            self.close()
        else:
            self.attempts += 1
            if self.attempts == self.max_attempts:
                QMessageBox.warning(self, 'Sorry', 'You\'ve used all your attempts. Better luck next time!')
                self.close()
            else:
                QMessageBox.warning(self, 'Incorrect', 'Incorrect guess. Try again.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = PasswordGame()
    game.show()
    sys.exit(app.exec_())
