import csv
import sys
from PyQt5 import uic
import pygame
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QMainWindow, QPushButton


class Circledrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(250, 250, 500, 500)
        self.setWindowTitle('кружки')

        self.trick_button = QPushButton(self)
        self.trick_button.resize(250, 50)
        self.trick_button.move(125, 125)
        self.trick_button.setText('нарисовать')
        self.trick_button.clicked.connect(self.run)

    def run(self):
        if self.trick_button.text() == 'нарисовать':
            self.trick_button.setText(':3')
            pygame.init()
            size = width, height = 500, 500
            screen = pygame.display.set_mode(size)
            for i in range(randint(1, 500)):
                pygame.draw.circle(screen, pygame.Color('yellow'), (randint(1, 500), randint(1, 500)), randint(50, 100))
            pygame.display.flip()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circledrawer()
    ex.show()
    sys.exit(app.exec())