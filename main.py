import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QBrush
from ui_file import Ui_MainWindow


class DrawingCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.lst = []

    def draw_circle(self):
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(65, self.height() - d)
        color = QColor(random.randint(0, 255), random.randint(0, 255),
                       random.randint(0, 255))
        self.lst.append((x, y, d, color))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, d, color in self.lst:
            painter.setBrush(QBrush(color))
            painter.setPen(color)
            painter.drawEllipse(x, y, d, d)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawingCircles()
    window.show()
    sys.exit(app.exec())
