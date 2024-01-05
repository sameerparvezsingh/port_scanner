from socket import *
import sys, time
from datetime import datetime

host = ''
max_port = 5000
min_port = 50

def scan_host(host, port, r_code=1):
    try:
        s = socket(AF_INET, SOCK_STREAM) #using OS scoket function to connect to intended target

        connection = s.connect_ex((host, port))

        if connection==0:
            r_code = connection
        s.close()
    except Exception as e:
        print(f"Error encountered: {e}")
    
    return r_code

try:
    host = input("[*] Enter target host address: *")
except KeyboardInterrupt:
    print("[*] Interupt detected. Exiting program.")
    sys.exit(1)

host_ip = gethostbyname(host)
print(f"\n[*] Host: {host}, IP:{host_ip}.")

print(f"**Starting scanning.**")

for port in range(min_port, max_port):
    try:
        response = scan_host(host, port)

        if response == 0:
            print(f"Port: {port} status = open")
    except Exception as e:
        print(f"The error is: {e}")