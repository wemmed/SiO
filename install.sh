#!/bin/bash
if [ "$EUID" -ne 0 ]; then
  exit 1
fi
apt-get update && apt-get install -y python3-pip python3-pyqt6
mkdir -p /usr/local/bin
cp sio.py /usr/local/bin/sio.py
chmod +x /usr/local/bin/sio.py
cp sio.desktop /usr/share/applications/sio.desktop
        