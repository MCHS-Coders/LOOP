import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from io import BytesIO
from get_weather import get_weather

# ---------- PyQt5 UI ----------
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Weather App")
window.resize(400, 300)

layout = QVBoxLayout()

city_input = QLineEdit()
city_input.setPlaceholderText("Enter city name")
layout.addWidget(city_input)

get_button = QPushButton("Get Weather")
get_button.clicked.connect(get_weather)
layout.addWidget(get_button)

result_label = QLabel("")
result_label.setAlignment(Qt.AlignCenter)
layout.addWidget(result_label)

icon_label = QLabel("")
layout.addWidget(icon_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
