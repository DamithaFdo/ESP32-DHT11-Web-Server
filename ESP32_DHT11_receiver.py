import socket

# Configure the UDP server
UDP_IP = "0.0.0.0"  # Listen on all network interfaces
UDP_PORT = 20001    # Match the port used in the Arduino code

# Create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}...")

while True:
    # Receive data from the ESP32
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message: {data.decode()} from {addr}")
