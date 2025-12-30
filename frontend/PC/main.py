## SKELETON ##

import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("AISES Team skeleton code becaue nobody bothered to do this part.")
window.resize(400, 300)
window.show()

sys.exit(app.exec_())
