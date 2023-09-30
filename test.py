from http.server import SimpleHTTPRequestHandler
import socketserver
import urllib.parse
import json
import socket
import sys

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

def scan_network(target_ip, port_list):
    for i in range(1, 255):
        ip = f"{target_ip}.{i}"
        for port in port_list:
            scan_port(ip, port)

    return 'string'

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Origin, Content-Type, Accept')
        super().end_headers()

    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Get the query parameters from the URL
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)

        # Get the 'ip' and 'port' parameters or use default values
        ip = query_params.get('ip', [''])[0]
        ports = query_params.get('port', [''])[0]


        #response_message = f'IP: {ip}, PORT: {port}'
        target_ip = ip
        ports_to_scan = [int(port) for port in ports.split(',')]  # Convert ports to integers
        resp = scan_network(target_ip, ports_to_scan)
        response_message = resp

        self.wfile.write(bytes(response_message, 'utf8'))
        
        return

PORT = 8000

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
