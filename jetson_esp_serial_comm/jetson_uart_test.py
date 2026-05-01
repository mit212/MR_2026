#!/usr/bin/env python3
# Make sure to install pyserial: pip3 install pyserial
import serial, time

# To find the ESP32 port on the Jetson run: ls /dev/ttyUSB* OR ls /dev/ttyACM* OR dmesg | grep tty
PORT = "/dev/ttyTHS0"   # Jetson’s hardware UART
BAUD = 115200 # Use the same baud for the Jetson and the ESP32!

ser = serial.Serial(PORT, BAUD, timeout=0.5)
print("Jetson TX/RX test – press Ctrl-C to quit")

try:
    while True:
        ser.write(b"HELLO\n")            # ➊ send a line
        print("TX: HELLO")

        resp = ser.readline().decode().strip() # ser.readline().decode('utf-8').strip()
        if resp:
            print("RX:", resp)           # expect “ACK HELLO”
        else:
            print("RX: (nothing)")

        time.sleep(1)                    # once per second
except KeyboardInterrupt:
    pass
finally:
    ser.close()
