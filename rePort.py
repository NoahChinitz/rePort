import socket
import time
import signal

# Class that passes an exception if we timeout
class TimeoutException(Exception):
    pass

# Actual timeout that raises the exception
def timeout_handler(signum, frame):
    raise TimeoutException

# Port scanning function that handles connection to specified IP
def rePort(port):
    # Create a socket connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # We need a signal here if we timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    try:
        # Sound the alarm if we take longer than one second
        signal.alarm(1)
        # Connect to the target IP and Port
        sock.connect((target_ip, port))
        # If seconds is zero, any pending alarm is canceled
        signal.alarm(0)
        # Return True if we have a successful connection
        return True
    except:
        # If we take longer than one second then we need to return False
        return False

# User Input
ip = input('Who do you want to scan?: ')
start_port = input('Starting Port?: ')
end_port = input('Ending Port?: ')

# Allows user to put in URL or IP
target_ip = socket.gethostbyname(ip)

# User Input
print('\nStarting scan on ' + str(target_ip))

# Start the timer
start = time.time()

# List to return all open ports
open_ports = []

# Go through the range of ports from start_port to end_port
for port in range(int(start_port), int(end_port)+1):
    print('Scanning port ' + str(port) + '...')
    if rePort(port):
        open_ports.append(port)
        print('Port ' + str(port) + ': open')
    else:
        print('Port ' + str(port) + ': closed')

# End the timer
end = time.time()

# Print out open ports
print('\nOpen Ports: ', open_ports)

# Print out time taken
print(f'Time Taken: {end-start:.4f} seconds')