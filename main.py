import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QBrush


class DrawingCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.lst = []

    def draw_circle(self):
        d = random.randint(0, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(0, self.height() - d)
        self.lst.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 220, 0)))
        painter.setPen(QColor(255, 220, 0))
        for x, y, d in self.lst:
            painter.drawEllipse(x, y, d, d)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawingCircles()
    window.show()
    sys.exit(app.exec())
