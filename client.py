import socket



serverAddressPort   = ("127.0.0.1", 8008)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 
def vib_once():
    msgFromClient       = str(3)
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print("just send 1")

def vib_update_freq(offset):
    msgFromClient       = str(offset)
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)



vib_once()


