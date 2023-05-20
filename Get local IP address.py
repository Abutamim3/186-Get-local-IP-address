'''
Python code 
Get local IP address
Developed by Abdul Rahman Al-Harbi


'''
import socket

def ip_check():
    """ uses the sockets module to find the local IP address """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Ping Google DNS server
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

print(ip_check())

print ("Developed by Abdul Rahman Al-Harbi")