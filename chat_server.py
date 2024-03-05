import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            break
        print(f"Message from {client_address}: {message}")
        client_socket.send(message.encode("utf-8"))  # Corrected line
    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
