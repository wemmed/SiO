#!/bin/bash
if [ "$EUID" -ne 0 ]; then
  exit 1
fi
rm -f /usr/local/bin/sio.py
rm -f /usr/share/applications/sio.desktop
