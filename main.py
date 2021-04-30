import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton

from home.views.VistaHome import VistaHome


if __name__ == '__main__':
  app = QApplication(sys.argv)
  vista_home = VistaHome()
  vista_home.show()
  sys.exit(app.exec_())



