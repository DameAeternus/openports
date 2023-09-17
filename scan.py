import socket
print("Script started.")
def scan_port(ip, port):
    print(f"Scanning port {port} on {ip}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip, port))
        print(f"Port {port} on {ip} is open")
        
    except socket.error:
        pass
    finally:
        sock.close()

def scan_network(target_ip,port_list):
    
    for i in range(1, 255):
        ip = f"{target_ip}.{i}"
        for port in port_list:
            scan_port(ip, port)
    
if __name__ == "__main__":
    target_ip = "192.168.1"  # Replace with your network range
    ports_to_scan = [80, 443, 22, 25,1414,14232]  # Add more ports if needed

    scan_network(target_ip, ports_to_scan)

