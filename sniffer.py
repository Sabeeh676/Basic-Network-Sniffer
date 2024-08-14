import socket
import struct

def sniff_packets(interface):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((interface, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    while True:
        packet, addr = s.recvfrom(65535)
        # Process the packet here
        print(packet[:20])

if __name__ == "__main__":
    interface = "your_interface_name"  # Replace with your network interface
    sniff_packets(interface)
