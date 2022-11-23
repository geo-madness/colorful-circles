import sys
from random import randint as rand

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen

WINDOW_HEIGHT, WINDOW_WIDTH = 400, 400
ELLIPSE_COLOR = QColor(255, 255, 0)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UI.ui", self)

        self.refresh_button.clicked.connect(self.on_refresh)

    def on_refresh(self):
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setPen(QPen(ELLIPSE_COLOR))

        for _ in range(5):
            diameter = rand(0, WINDOW_WIDTH)
            x, y = rand(0, WINDOW_WIDTH), rand(0, WINDOW_HEIGHT)
            qp.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
