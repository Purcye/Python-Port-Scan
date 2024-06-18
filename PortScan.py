import socket
import datetime

target = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

print(f"Scanning target {target} from port {start_port} to {end_port}....")

x = datetime.datetime.now()
date = x.strftime("%x").replace("/", "-")
time = x.strftime("%X").replace(":", "-")

filename = f"Port Scan (Date {date}, Time {time}).txt"

with open(filename, "w") as f:
    f.write(f"Target IP address: {target}\n")
    f.write(f"Port Range: {start_port} - {end_port}\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            service = socket.getservbyport(port)
            print(f"Port {port} is open - Service: {service}")
            f.write(f"\nPort {port} is open - Service: {service}")
        else:
            print(f"Port {port} is closed")
            f.write(f"\nPort {port} is closed")

        sock.close()

print(f"\nScan results saved in {filename}")
