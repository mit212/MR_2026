# MR_2026
Some helpful code for the Mobile Robot. Particularly, communicating between the ESP32 and the Jetson Nano

## 1 Common Issues (and fixes) for Jetson and ESP32 Comms
1. Permission denied: Try `sudo usermod -a -G dialout $USER`
2. Wrong baud rate: Make sure both the Jetson and ESP32 use baud rate `115200`
3. ESP32 resets when opening serial: This is normal due to DTR/RTS signals. You can ignore it or disable auto-reset if needed
4. Garbage data: Usually mismatched baud rate or encoding
