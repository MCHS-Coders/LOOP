import json
import time
from threading import Event

import meshtastic
import meshtastic.serial_interface
from pubsub import pub


class LoRaClient:
    def __init__(self, port=None):
        # Auto-detect USB device if port is None
        self.iface = meshtastic.serial_interface.SerialInterface(port)
        self._response = None
        self._waiter = Event()

        pub.subscribe(self._on_receive, "meshtastic.receive")

    def _on_receive(self, packet, interface):
        try:
            text = packet.get("decoded", {}).get("text")
            if not text:
                return

            data = json.loads(text)

            if data.get("type") == "weather_resp":
                self._response = data
                self._waiter.set()

        except Exception:
            pass

    def request_weather(self, city, timeout=10):
        self._response = None
        self._waiter.clear()

        payload = {
            "type": "weather_req",
            "city": city
        }

        self.iface.sendText(json.dumps(payload))

        if not self._waiter.wait(timeout):
            return None

        return {
            "temp": self._response["temp"],
            "desc": self._response["desc"],
            "icon": self._response["icon"]
        }
