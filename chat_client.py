import socket

def main():
    host = "127.0.0.1"
    port = 12345
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Connected to server")
        while True:
            message = input("You: ")
            client_socket.send(message.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8")
            print("Server:", response)
            if message.lower() == "exit":
                break
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
