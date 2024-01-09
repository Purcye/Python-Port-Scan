# Python-Port-Scan
Simple python port scanner, that exports results into a text document with the date and time!

### Importing Modules:
    import socket
    import datetime
- The socket module provides a way to work with sockets, which are endpoints for sending or receiving data
across a computer network.
- The datetime module is used for working with dates and times.
### User Input:

    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

-  Asks the user to input the target IP address, starting port number, and ending port number.
Print Statement:
print(f"Scanning target {target} from port {start_port} to {end_port}....")
- Prints a message indicating the target IP address and port range that will be scanned.
### File Handling:

    x = datetime.datetime.now()
    date = (x.strftime("%x"))
    time = (x.strftime("%X"))
    title = date.replace("/","-")
    title2 = time.replace(":","-")
    f = open("Port Scan (Date " + title + "," + " Time " + title2 + ").txt", "x")

- Gets the current date and time using datetime.datetime.now().
- Formats the date and time to replace characters that might cause issues in a filename.
- Opens a file for writing with a filename based on the date and time.
### Writing to the File:

    f.write("Target IP address: " + target)
    f.write("\nPort Range: " + str(start_port) + " - " + str(end_port) + "\n")
- Writes the target IP address and port range information to the file.
### Port Scanning Loop:

    for port in range(start_port, end_port + 1):
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sock.settimeout(1)
     result = sock.connect_ex((target, port))
     if result == 0:
     print(f"Port {port} is open")
     f.write(f"\nPort {port} is open")
     else:
     print(f"Port {port} is closed")
     f.write(f"\nPort {port} is closed")

- Iterates through each port in the specified range.
- Creates a socket and attempts to connect to the target IP address and port.
- If the connection attempt is successful (result is 0), it prints that the port is open and writes it to the file. Otherwise, it prints that the port is closed and writes it to the file.
