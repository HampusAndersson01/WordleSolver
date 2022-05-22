import sys
import re

from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGroupBox, QWidget, QLabel, QVBoxLayout, QSizePolicy
)
from window import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.words = []
        self.loadWords()
        self.setupUi(self)
        self.setupGUI()
        self.initGui()
        self.currentRow = 1
        self.reset()

        self.firstGuess()

    def reset(self):
        self.correctWord = ["", "", "", "", ""]
        self.correctLetters = [[], [], [], [], []]
        self.wrongLetters = []
        self.currentRowState = ["", "", "", "", ""]
        self.guess = ["", "", "", "", ""]
        self.badWords = []

        for row in range(1, 7):
            self.makeGuess(self.guess, row)
            for col in range(1, 6):
                self.currentRow = row
                self.setColor(col, "white")

        self.currentRow = 1
        self.firstGuess()

    def loadWords(self):
        file1 = open('words5.txt', 'r')
        Lines = file1.readlines()

        for line in Lines:
            self.words.append(line.strip())

    def setupGUI(self):
        self.labelList = []

        for child in self.centralwidget.children():
            if isinstance(child, QGroupBox):
                vbox = QVBoxLayout()
                # print(child.objectName())
                self.labelList.append(QLabel(""))
                self.labelList[len(self.labelList) - 1].setAlignment(Qt.AlignCenter)
                self.labelList[len(self.labelList) - 1].setFont(QFont('Times', 30))
                self.labelList[len(self.labelList) - 1].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                child.setLayout(vbox)
                vbox.addWidget(self.labelList[len(self.labelList) - 1])

    def initGui(self):
        self.doneBtn.clicked.connect(self.startNextTry)
        self.newBtn.clicked.connect(self.newWord)

        self.col1Gray.clicked.connect(lambda: self.setColor(1, "gray"))
        self.col2Gray.clicked.connect(lambda: self.setColor(2, "gray"))
        self.col3Gray.clicked.connect(lambda: self.setColor(3, "gray"))
        self.col4Gray.clicked.connect(lambda: self.setColor(4, "gray"))
        self.col5Gray.clicked.connect(lambda: self.setColor(5, "gray"))
        self.col1Orange.clicked.connect(lambda: self.setColor(1, "orange"))
        self.col2Orange.clicked.connect(lambda: self.setColor(2, "orange"))
        self.col3Orange.clicked.connect(lambda: self.setColor(3, "orange"))
        self.col4Orange.clicked.connect(lambda: self.setColor(4, "orange"))
        self.col5Orange.clicked.connect(lambda: self.setColor(5, "orange"))
        self.col1Green.clicked.connect(lambda: self.setColor(1, "green"))
        self.col2Green.clicked.connect(lambda: self.setColor(2, "green"))
        self.col3Green.clicked.connect(lambda: self.setColor(3, "green"))
        self.col4Green.clicked.connect(lambda: self.setColor(4, "green"))
        self.col5Green.clicked.connect(lambda: self.setColor(5, "green"))

    def setColor(self, col, color):
        """

        :param col:
        :type col: int
        :param color:
        :type color: str
        :return:
        """
        string = "row{}col{}".format(self.currentRow, col)
        btn = getattr(self, string)
        for child in btn.children():
            if isinstance(child, QLabel):
                child.setStyleSheet("background-color:{};".format(color))
                self.currentRowState[col - 1] = color

    def startNextTry(self):
        if self.currentRow < 7:
            for i in range(5):
                if self.currentRowState[i] == "green":
                    self.correctWord[i] = self.guess[i]
                elif self.currentRowState[i] == "orange":
                    for n in range(5):
                        if i != n:
                            self.correctLetters[n].append(self.guess[i])
                elif self.currentRowState[i] == "gray":
                    if self.guess[i] not in self.correctWord:
                        self.wrongLetters.append(self.guess[i])
            for i in range(5):
                if self.correctWord[i] != "":
                    self.correctLetters[i] = [self.guess[i]]
            print("WRONG LETTERS: ", self.wrongLetters)
            print("CORRECT WORD: ", self.correctWord)
            self.currentRow += 1
            self.currentRowState = ["", "", "", "", ""]
            if "" not in self.correctWord:
                self.reset()
            else:
                self.findNextGuess()

    def newWord(self):
        self.badWords.append("".join(self.guess))
        self.findNextGuess()

    def makeGuess(self, guess, row=-1):
        """

        :param guess:
        :type guess: list
        :param row:
        :type row: int
        :return:
        """
        if row == -1:
            row = self.currentRow
        for col in range(1, 6):
            string = "row{}col{}".format(row, col)
            btn = getattr(self, string)
            for child in btn.children():
                if isinstance(child, QLabel):
                    child.setText(guess[col - 1].upper())

    def firstGuess(self):
        starterWord = "crane"
        self.guess = list(starterWord)
        self.makeGuess(self.guess, self.currentRow)

    def checkIfDone(self):
        for letter in self.correctWord:
            if letter == "":
                return False
        return True

    def findNextGuess(self):
        if self.checkIfDone():
            self.makeGuess(self.correctWord, self.currentRow)
        else:
            wordScore = {}
            for word in self.words:
                if word not in self.badWords:
                    score = 0
                    wrong = False
                    for letter in self.wrongLetters:
                        if letter in word:
                            wrong = True
                        break
                    if wrong:
                        continue
                    for index, letter in enumerate(list(word)):
                        if letter in self.correctLetters[index]:
                            score += 1
                        if letter in self.correctWord[index]:
                            score += 3
                        if letter in self.wrongLetters:
                            score -= 10

                    wordScore[word] = score
            # print(wordScore)
            bestWord = ""
            bestScore = -1

            for word, point in wordScore.items():
                correctPossibleWord = True
                for index, letter in enumerate(list(word)):
                    if self.correctWord[index] != "":
                        if self.correctWord[index] == letter:
                            correctPossibleWord = True
                            break

                        else:
                            correctPossibleWord = False
                    if letter in self.wrongLetters:
                        correctPossibleWord = False
                        break

                if point > bestScore and correctPossibleWord and word not in self.wrongLetters:
                    bestScore = point
                    bestWord = word
            print("Best word: ", list(bestWord))
            print("", list(bestWord))
            self.guess = list(bestWord)
            self.makeGuess(self.guess)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
