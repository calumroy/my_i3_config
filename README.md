
# My i3 Config

This repository contains my customized configuration for the [i3 window manager](https://i3wm.org/). It includes key bindings, layouts, and scripts for features like Bluetooth management, system notifications, and more.

## Purpose

- **Version Control**: Keep track of and back up my i3 configuration.
- **Portability**: Easily apply the same i3 setup on different machines.
- **Extendability**: Integrate scripts (e.g., custom Bluetooth status) and additional tools (e.g., py3status) into i3.

## Dependencies & Requirements

1. **i3 Window Manager**  
   - Typically installed via your package manager:  
     ```bash
     sudo apt install i3
     ```
2. **py3status** (if using the custom bar modules)  
   - For Debian/Ubuntu:  
     ```bash
     sudo apt install py3status
     ```
3. **Bluetooth Tools** (if using the Bluetooth status script)  
   - E.g., `bluetoothctl`, `bluez`, `bluedevil-wizard`:
     ```bash
     sudo apt install bluetooth bluez bluedevil
     ```
4. **Optional Notification Daemon** (e.g., `dunst`) if you want native notifications:
   ```bash
   sudo apt install dunst
   ```
   Add this to your i3 config:
   ```bash
   exec --no-startup-id dunst
   ```
5. **Fonts**  
   - To ensure icon glyphs (e.g., Font Awesome icons) work in the i3bar, install a font with icons:
     ```bash
     sudo apt install fonts-font-awesome
     ```
   - Or use [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) for broader icon support.

## How to Use

1. **Clone this repository**:
   ```bash
   git clone https://github.com/calumroy/my_i3_config.git ~/Documents/projects/my_i3_config
   ```
2. **Symlink the config** to your `~/.config/i3/` directory:
   ```bash
   cd ~/Documents/projects/my_i3_config
   ln -s ~/Documents/projects/my_i3_config/i3/* ~/.config/i3/
   ```
   This creates symbolic links so that i3 loads the files directly from this repo.
3. **Restart/Reload i3**:
   - Press `Mod + Shift + r` (usually `Super + Shift + r`) to reload i3, or log out and log back in to i3.

### Directory Structure

```
my_i3_config/
├── i3/
│   └── config              # Main i3 configuration file
├── scripts/                # Custom scripts (if any)
├── README.md               # This file
└── ...                     # Other files or folders
```

- **i3/config**: Your main i3 config with key bindings, bar settings, etc.

## Notes

- **Custom Bluetooth Module**: If you have included a script or module (e.g., `bluetooth_status.py`) for py3status, place it in `~/.config/py3status/` or ensure your i3 config points to it correctly.
- **Updating**: Any changes committed and pushed to this repository will automatically reflect if you symlinked your config. Just pull the latest changes and reload i3.
- **Troubleshooting**: If something isn’t working (e.g., fonts or icons not displaying), verify you have the right packages installed and that your i3 font line references the installed fonts (e.g., `font pango:DejaVu Sans Mono 10, FontAwesome 10`).

## Contributing

- **Issues/Requests**: Feel free to open an issue or pull request if you have suggestions on improvements or additional features.

