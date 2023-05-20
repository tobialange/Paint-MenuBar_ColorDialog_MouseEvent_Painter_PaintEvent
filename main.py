import sys
from PySide6 import QtWidgets
from MyMainWindow import MyMainWindow

# All you need is
# https://doc.qt.io/qtforpython/

app = QtWidgets.QApplication(sys.argv)
dialog = MyMainWindow()
dialog.show()
sys.exit(app.exec())
