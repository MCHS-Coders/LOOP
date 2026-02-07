import meshtastic.serial_interface
from pubsub import pub


class LoRaClient:
    def __init__(self, port=None, prefix="snow"):
        self.prefix = prefix.lower()
        self.iface = meshtastic.serial_interface.SerialInterface(port)

        self._connected_node = None
        pub.subscribe(self._on_packet, "meshtastic.receive")

    def close(self):
        pub.unsubscribe(self._on_packet, "meshtastic.receive")
        if self.iface:
            self.iface.close()

    def _on_packet(self, packet, interface):
        frm = packet.get("fromId")
        if not frm:
            return

        node = interface.nodes.get(frm)
        if not node:
            return

        name = (
            node.get("user", {}).get("longName")
            or node.get("user", {}).get("shortName")
            or ""
        ).lower()

        if name.startswith(self.prefix):
            self._connected_node = node

    def get_weather_station(self):
        return self._connected_node
