# -*- coding: utf-8 -*-
import subprocess

class Py3status:
    """
    A py3status module to show and control Bluetooth status.
    Left-click: toggle on/off
    Right-click: open bluedevil-wizard
    """

    # Called by py3status to get module output
    def bluetooth_status(self):
        # Check if powered on:
        powered_on = self._bluetooth_is_on()

        # Decide what to display
        if powered_on:
            # Font Awesome Bluetooth icon
            # Make sure your bar font supports this glyph
            icon = ""
            text = f"{icon} On"
            color = "#00ff00"  # green
        else:
            icon = ""
            text = f"{icon} Off"
            color = "#ff0000"  # red

        return {
            "full_text": text,
            "color": color,
            # Tells py3status when to call us again.
            "cached_until": self.py3.time_in(5),  # update every 5s
        }

    # Handle clicks from the bar
    def on_click(self, event):
        button = event["button"]
        if button == 1:
            # Left-click → toggle power
            self._toggle_bluetooth()
        elif button == 3:
            # Right-click → open wizard
            subprocess.Popen(["bluedevil-wizard"])

    # Helper: check if bluetooth is on
    def _bluetooth_is_on(self):
        try:
            output = subprocess.check_output(["bluetoothctl", "show"], text=True)
            return "Powered: yes" in output
        except Exception:
            return False
    
    def _toggle_bluetooth(self):
        if self._bluetooth_is_on():
            # Turn off, discard output
            subprocess.run(
                ["bluetoothctl", "power", "off"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        else:
            # Turn on, discard output
            subprocess.run(
                ["bluetoothctl", "power", "on"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
