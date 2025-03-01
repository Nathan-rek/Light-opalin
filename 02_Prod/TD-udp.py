import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 9500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    try:
        decoded_data = data.decode('utf-8', 'ignore')
        print("received messages: %s" % decoded_data)
    except Exception as e:
        print("Failed to decode data: ", str(e))
   