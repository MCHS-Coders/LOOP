import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from io import BytesIO

def get_weather():
    city = city_input.text().strip()
    if not city:
        result_label.setText("Please enter a city name.")
        icon_label.clear()
        return

    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key (this is fine for now)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            result_label.setText("City not found.")
            icon_label.clear()
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        icon_code = data["weather"][0]["icon"]

        result_label.setText(f"{city}: {temp}°C, {desc.capitalize()}")

        # Fetch weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_data = requests.get(icon_url).content
        pixmap = QPixmap()
        pixmap.loadFromData(icon_data)
        icon_label.setPixmap(pixmap)
        icon_label.setAlignment(Qt.AlignCenter)

    except Exception as e:
        result_label.setText("Error fetching weather.")
        icon_label.clear()

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
