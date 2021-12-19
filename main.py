import threading
from queue import Queue
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


def scanner(port):
    for port in range(1, final_range):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((IP_address, port))
        if result == 0:
            print("Port " + str(port) + " open")
        else:
            print("Port " + str(port) + " closed")
        sock.close()
print ("Found in "+ str(time.time() - time_start) + " sec")

if __name__ == "__main__":
    for port in range(100):
        scanner(port)

lock = threading.lock()
q = Queue()

def threader():
    while True:
        port = q.get()
        scanner(port)
        q.task_done()

def main():
    for i in range(10):
        thread = threading.Thread(target = threader)
        thread.daemon = True
        thread.start ()

    for port in range(final_range):
        q.put(port)
    q.join()
pass
