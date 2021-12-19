import socket
import time

time_start = time.time()
ans = input("Do you know your IP address--y/n:")
if ans == "y":
    IP_address = input("Enter IP address:")
elif ans == "n":
    server_url = input("Enter a remote host to scan: ")
    IP_address = socket.gethostbyname(server_url)

port_range = input("Run up to port #:")
final_range = (int(port_range))+1

for port in range (1, final_range):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((IP_address, port))
    if result == 0:
        print ("Port "+str(port)+" open")
    else:
        print("Port " + str(port) + " closed")
    sock.close()
print ("Found in "+ str(time.time() - time_start))