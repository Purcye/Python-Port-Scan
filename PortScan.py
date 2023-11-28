import socket
import datetime

target = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

print(f"Scanning target {target} from port {start_port} to {end_port}....")

x = datetime.datetime.now()
date = (x.strftime("%x"))
time = (x.strftime("%X"))
title = date.replace("/","-")
title2 = time.replace(":","-")


f = open("Port Scan (Date " + title + "," + " Time " + title2+").txt", "x")
f.write("Target IP address: " + target)
f.write("\nPort Range: " + str(start_port) + " - " + str(end_port)+"\n")

for port in range(start_port,end_port+1):
 sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 sock.settimeout(1)
 result = sock.connect_ex((target, port))
 if result == 0:
  print(f"Port {port} is open")
  f.write(f"\nPort {port} is open")
 else:
  print(f"Port {port} is closed")
  f.write(f"\nPort {port} is closed")

f.close()


























