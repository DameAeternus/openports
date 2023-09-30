import socket
import sys

print("Script started.")

def scan_port(ip, port):
    print(f"Scanning port {port} on {ip}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip, port))
        print(f"Port {port} on {ip} is open")
#       build a string
#       return
    except socket.error:
        pass
    finally:
        sock.close()

def scan_network(target_ip, port_list):
    for i in range(1, 255):
        ip = f"{target_ip}.{i}"
        for port in port_list:
            scan_port(ip, port)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scan.py <target_ip> <port1,port2,port3,...>")
        sys.exit(1)

    target_ip = sys.argv[1]
    ports_to_scan = [int(port) for port in sys.argv[2].split(',')]  # Convert ports to integers

    scan_network(target_ip, ports_to_scan)
