import socket
import subprocess
import sys
from datetime import datetime

# Common ports and their functions
common_ports = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    # Add more later
}

# Blank your screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print banner with info on which host we're going to scan
print(" " * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("_" * 60)

# Check date and time the scan started
t1 = datetime.now()

# Using range function specify ports
# Also we'll do error handling

try:
    for port in range (1, 100):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            service = common_ports.get(port, "Unknown Service")
            print(f"Port {port}: Open ({service})")
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not e resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Check time again
t2 = datetime.now()

# Calculate time difference to see how long scan is
total = t2 - t1

# Display info on screen
print("Scanning completed in: ", total)