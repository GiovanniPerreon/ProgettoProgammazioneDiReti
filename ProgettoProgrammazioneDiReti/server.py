import os
import datetime
from socket import *
HOST = "localhost"
PORT = 8080
BASE_DIR = "www"
SEPARATOR = os.sep

MIME_TYPES = {
    ".html": "text/html",
    ".css": "text/css",
    ".jpg": "image/jpeg",
    ".png": "image/png",
    ".ico": "image/x-icon",
}

def get_mime_type(file_path):
    ext = os.path.splitext(file_path)[1]
    return MIME_TYPES.get(ext, "application/octet-stream")

def handle_request(connection, ip):
    try:
        request = connection.recv(1024).decode()
        if len(request.split()) > 0:
            request_line = request.split("\r\n")[0]
            print("Request:", request_line)
            method, path, _ = request_line.split()
        if path == "/":
            path = "/index.html"
        file_path = BASE_DIR + SEPARATOR + path.lstrip("/")

        if os.path.isfile(file_path):
            f = open(file_path, "rb")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            outputdata = f.read()
            mime_type = get_mime_type(file_path)
            headers = (
                f"HTTP/1.1 200 OK\r\n"
                f"Date: {timestamp}\r\n"
                f"Content-Type: {mime_type}\r\n"
                f"Content-Length: {len(outputdata)}\r\n"
                f"Connection: close\r\n"
                f"\r\n"
            )
            connection.send(headers.encode())
            print("Response to", ip, "at", timestamp)
            print(" 200 OK - File found:", file_path)
        else:
            outputdata = b"<h1>404 Not Found</h1>"
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            connection.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n","UTF-8"))
            print("Response to", ip, "at", timestamp)
            print(" 404 Not Found - File missing:", file_path)
        connection.send(outputdata)

    except Exception as e:
        print("Error:", e)
    finally:
        connection.close()

def run_server():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen()
    print(f"Server listening on http://{HOST}:{PORT}")

    while True:
        connectionSocket, addr = serverSocket.accept()
        ip = addr[0]
        handle_request(connectionSocket, ip)

run_server()
