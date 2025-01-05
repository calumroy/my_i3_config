# -*- coding: utf-8 -*-
import subprocess
import time

class Py3status:
    """
    Bluetooth module for py3status with an 'expanded' mode.
    Left-click: toggle power
    Middle-click: show connected devices in i3bar (for 5s)
    Right-click: open bluedevil-wizard
    """

    # How many seconds to display connected devices
    EXPANDED_DURATION = 5

    def post_config_hook(self):
        # Initialize state
        self.expanded = False
        self.expanded_since = 0
        self.connected_info = None

    def bluetooth_status(self):
        """
        Return either the normal "BT On/Off" text or the expanded device list
        (if the user middle-clicked in the last X seconds).
        """

        now = time.time()

        # If we are in expanded mode, check if time has elapsed
        if self.expanded:
            if (now - self.expanded_since) < self.EXPANDED_DURATION:
                # Still within expanded view, show connected devices
                if not self.connected_info:
                    # Fallback if we have no info
                    text = "No connected devices"
                else:
                    # For example, show them all on one line
                    text = "Connected: " + ", ".join(self.connected_info)
                return {
                    "full_text": text,
                    "color": "#00FFFF",  # e.g., cyan
                    "cached_until": self.py3.time_in(1),
                }
            else:
                # Time’s up; revert to normal display
                self.expanded = False
                self.connected_info = None

        # Normal display (On/Off)
        powered_on = self._bluetooth_is_on()
        if powered_on:
            icon = ""  # Requires a font that supports this glyph
            text = f"{icon} On"
            color = "#00FF00"
        else:
            icon = ""
            text = f"{icon} Off"
            color = "#FF0000"

        return {
            "full_text": text,
            "color": color,
            "cached_until": self.py3.time_in(5),
        }

    def on_click(self, event):
        button = event["button"]
        if button == 1:
            # Left-click → toggle power
            self._toggle_bluetooth()
        elif button == 2:
            # Middle-click → gather connected devices, show them for 5s
            self._expand_connected_devices()
        elif button == 3:
            # Right-click → open wizard
            subprocess.Popen(["bluedevil-wizard"])

    def _expand_connected_devices(self):
        """Fetch connected devices and switch to expanded view."""
        try:
            output = subprocess.check_output(
                ["bluetoothctl", "devices", "Connected"],
                text=True
            ).strip()
            if output:
                # Each line looks like: "Device XX:XX:XX:XX:XX:XX DeviceName"
                lines = output.splitlines()
                # Parse each line to extract just the "DeviceName" or everything
                connected = []
                for line in lines:
                    # e.g., line = "Device 12:34:56:78:9A:BC MyHeadset"
                    parts = line.split(" ", 2)  # split into 3 parts max
                    if len(parts) == 3:
                        # e.g. ["Device", "12:34:56:78:9A:BC", "MyHeadset"]
                        connected.append(parts[2])  # "MyHeadset"
                    else:
                        connected.append(line)       # fallback
                self.connected_info = connected
            else:
                self.connected_info = ["None"]
        except subprocess.CalledProcessError:
            self.connected_info = ["Error listing devices"]

        # Set expanded mode + time
        self.expanded = True
        self.expanded_since = time.time()

    def _bluetooth_is_on(self):
        try:
            output = subprocess.check_output(["bluetoothctl", "show"], text=True)
            return "Powered: yes" in output
        except Exception:
            return False

    def _toggle_bluetooth(self):
        # Avoid polluting the JSON stream with bluetoothctl output
        if self._bluetooth_is_on():
            subprocess.run(
                ["bluetoothctl", "power", "off"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        else:
            subprocess.run(
                ["bluetoothctl", "power", "on"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

