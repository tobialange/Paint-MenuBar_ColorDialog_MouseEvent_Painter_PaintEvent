from PySide6.QtWidgets import QMainWindow, QMenuBar, QColorDialog, QFileDialog, QLabel
from PySide6.QtGui import QMouseEvent, QPainter, QPaintEvent, QPixmap, QColor

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # See https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMenuBar.html?highlight=qmenubar
        # for None parent
        self.menu_bar = QMenuBar(None)

        self.fileMenu = self.menu_bar.addMenu("Bilder")

        self.action_load_file = self.fileMenu.addAction("Bild öffnen", self.load_file)
        self.action_save_file = self.fileMenu.addAction("Bild speichern", self.save_file)

        self.fileMenu.addAction("Farbe", self.setColor)

        self.setMenuBar(self.menu_bar)

        self.setWindowTitle("M$ P41nt")

        self.pos = None
        self.color = QColor("green")
        self.canvas = QPixmap("./Fisch.jpg")

        self.draw_widget = QLabel(self)
        self.draw_widget.setPixmap(self.canvas)
        self.setCentralWidget(self.draw_widget)

    def setColor(self):
        selected_color = QColorDialog.getColor(self.color, self, "Farbe wählen")

        if selected_color.isValid():
            self.color = selected_color

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.pos = ev.pos()

        self.update()

    def paintEvent(self, ev: QPaintEvent) -> None:
        painter = QPainter(self.canvas)

        if self.pos:
            painter.setPen(self.color)
            painter.drawEllipse(self.pos, 20, 20)

        painter.end()
        self.draw_widget.setPixmap(self.canvas)

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Bild auswählen", "Bilder (*.png, *.jpg)")

        if file_name:
            self.canvas = QPixmap(file_name)
            self.setPixmap(self.canvas)

            self.update()

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Bild speichern", "./", "Bilder (*.png, *.jpg)")

        self.canvas.save("./test1234.jpg")
