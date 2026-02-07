import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QFrame
)
from PyQt5.QtCore import QTimer, Qt

from lora_utils import LoRaClient


class WeatherUI(QWidget):
    POLL_MS = 3000

    def __init__(self):
        super().__init__()

        self.client = LoRaClient()
        self.current_node = None

        self.setWindowTitle("Mesh Weather")
        self.setFixedSize(360, 200)

        self._build_ui()
        self._start_timer()

    # ---------- UI ----------

    def _build_ui(self):
        self.title = QLabel("Weather Mesh")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName("title")

        self.status = QLabel("Searching for stations…")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setObjectName("status")

        card = QFrame()
        card.setObjectName("card")

        card_layout = QVBoxLayout(card)
        card_layout.addWidget(self.title)
        card_layout.addWidget(self.status)

        layout = QVBoxLayout(self)
        layout.addStretch()
        layout.addWidget(card)
        layout.addStretch()

        self.setStyleSheet("""
            QWidget {
                background: #1e1e1e;
                color: #e6e6e6;
                font-family: Segoe UI, Arial;
            }
            #card {
                background: #2a2a2a;
                border-radius: 10px;
                padding: 18px;
            }
            #title {
                font-size: 18px;
                font-weight: 600;
            }
            #status {
                font-size: 15px;
            }
        """)

    # ---------- polling ----------

    def _start_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._refresh)
        self.timer.start(self.POLL_MS)

    def _refresh(self):
        node = self.client.find_weather_station()

        # Only update UI when something changes
        if node != self.current_node:
            self.current_node = node
            self._update_status(node)

    def _update_status(self, node):
        if node:
            name = node.get("user", {}).get("longName", "Unknown")
            self.status.setText(f"Connected to {name}")
        else:
            self.status.setText("No weather stations found")

    # ---------- cleanup ----------

    def closeEvent(self, event):
        self.client.close()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WeatherUI()
    w.show()
    sys.exit(app.exec_())
