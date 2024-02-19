from RF24 import *
import time
import sqlite3

radio = RF24(22, 0)  # CE, CSN pins

pipes = [b"00001", b"00002"]  # Addresses should match the Arduino's

radio.begin()
radio.setPALevel(RF24_PA_MAX)  # Power Amplifier level
radio.setChannel(0x76)  # Again, ensure it matches the Arduino's channel
radio.openReadingPipe(1, pipes[0])  # We listen on the first pipe
radio.startListening()  # Start listening for messages
radio.openReadingPipe(1, pipes[0])
radio.enableDynamicPayloads()  # Enable dynamic payloads


import struct

conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()

# Create table to store sensor data (only if it does not exist)
c.execute('''CREATE TABLE IF NOT EXISTS sensor_data
             (timestamp DATETIME, sensor1 INTEGER, sensor2 INTEGER, sensor3 INTEGER)''')
conn.commit()

def save_data(sensor1, sensor2, sensor3):
    """Save the sensor data to the SQLite database."""
    c.execute("INSERT INTO sensor_data (timestamp, sensor1, sensor2, sensor3) VALUES (datetime('now'), ?, ?, ?)",
              (sensor1, sensor2, sensor3))
    conn.commit()

def receive_message():
    while not radio.available():
        time.sleep(1/100)
    received_payload = radio.read(radio.getDynamicPayloadSize())

    # Adjust the unpack format based on the actual data size and type
    if len(received_payload) == 6:  # Assuming each integer is 2 bytes
        # Unpack 3 signed short integers from received payload
        sensor1, sensor2, sensor3 = struct.unpack('<3h', received_payload)
        print(f"Received data - Sensor1: {sensor1}, Sensor2: {sensor2}, Sensor3: {sensor3}")
        save_data(sensor1, sensor2, sensor3)
    else:
        print("Received data of unexpected size.")

while True:
    receive_message()
    time.sleep(1)

'''
def receive_message():
    while not radio.available():
        time.sleep(1/100)
    received_payload = radio.read(radio.getDynamicPayloadSize())
    #print("Payload size:", len(received_payload))  # Debug payload size

    if len(received_payload) == 2:
        # Assuming the data is a 2-byte integer (signed or unsigned)
        value, = struct.unpack('h', received_payload)  # 'h' for signed short, 'H' for unsigned
        print("Received value:", value)
    else:
        print("Received data of unexpected size.")
'''

print('Raspberry Pi NRF24L01 Receiver Started')
try:
    while True:
        receive_message()
except KeyboardInterrupt:
    radio.powerDown()
