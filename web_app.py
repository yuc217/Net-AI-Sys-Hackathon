import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connected to: {client_address}")

    while True:
        # Receive data
        received_data = client_socket.recv(1024).decode()
        if not received_data:
            break
        print(f"Received data from {client_address}: {received_data}")

        # Analyze data and visualize it
        # Perform your data analysis and visualization operations here

        # Reply message
        response_message = "Message received successfully!"
        client_socket.sendall(response_message.encode())

    # Close connection
    client_socket.close()
    print(f"Connection with {client_address} closed.")

def start_server():
    # Raspberry Pi devices IP addresses and ports
    raspberry_pis = {
        'device1': '192.168.50.107',
        'device2': '192.168.50.216',
        'device3': '192.168.50.127'
        
    }
    port_number = 60000  # Same port number for all devices

    # Create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind IP address and port
    server_socket.bind(('0.0.0.0', port_number))

    # Start listening
    server_socket.listen()
    print("Waiting for messages...")

    while True:
        # Accept connection
        client_socket, client_address = server_socket.accept()

        # Start a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    # Start the server
    start_server()
