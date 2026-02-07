import meshtastic.serial_interface
from pubsub import pub


class LoRaClient:
    def __init__(self, port=None, prefix="mini-weather-"):
        self.prefix = prefix.lower()
        self.iface = meshtastic.serial_interface.SerialInterface(port)

        self._nodes = {}
        pub.subscribe(self._on_node_updated, "meshtastic.node.updated")

    # ---------- lifecycle ----------

    def close(self):
        """Clean shutdown."""
        pub.unsubscribe(self._on_node_updated, "meshtastic.node.updated")
        if self.iface:
            self.iface.close()

    # ---------- pubsub ----------

    def _on_node_updated(self, node, interface):
        if not node:
            return
        self._nodes[node.get("num")] = node

    # ---------- public API ----------

    def find_weather_station(self):
        """Return first matching weather node or None."""
        for node in self._nodes.values():
            if self._is_weather_node(node):
                return node
        return None

    def get_all_weather_stations(self):
        """Return list of all matching nodes."""
        return [n for n in self._nodes.values() if self._is_weather_node(n)]

    # ---------- helpers ----------

    def _is_weather_node(self, node):
        user = node.get("user", {})
        name = (
            user.get("longName")
            or user.get("shortName")
            or ""
        ).lower()

        # NOT NEEDED FOR POC
        return True # name.startswith(self.prefix)
