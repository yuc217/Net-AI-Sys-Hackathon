import socket
import streamlit as st
from datetime import datetime
from visualizations import generate_image

def handle_client(client_socket, client_address, raspberry_pis):
    st.write(f"Connected to: {client_address}")

    while True:
        received_data = client_socket.recv(1024).decode()
        if not received_data:
            break
        
        # get device name
        device_name = None
        for name, ip in raspberry_pis.items():
            if ip == client_address[0]:
                device_name = name
                break

        # display received data
        if device_name:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.subheader(device_name)
            st.write(f"{timestamp} - Received data from {client_address}: {received_data}")

            # reply to nodes
            response_message = "Message received successfully!"
            client_socket.sendall(response_message.encode())
        else:
            st.write(f"Unknown device with IP {client_address[0]}")

    client_socket.close()
    st.write(f"Connection with {client_address} closed.")

def display_current_content():
    # RPIs info
    raspberry_pis = {
        'device1': '192.168.50.107',
        'device2': '192.168.50.216',
        'device3': '192.168.50.127'  
    }
    port_number = 60000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind(('0.0.0.0', port_number))
        server_socket.listen()
        st.write("Waiting for messages...")
        while True:
            client_socket, client_address = server_socket.accept()
            handle_client(client_socket, client_address, raspberry_pis)
    finally:
        server_socket.close()

def display_image():
    st.write("Image Tab")
    st.write("Generating image...")
    # using function from visualizations.py
    fig = generate_image()
    fig_path = "generated_image.png"
    fig.savefig(fig_path)
    st.image(fig_path, caption="Generated Image")

if __name__ == "__main__":
    option = st.selectbox(
        "Select tab",
        ("Current Content", "Image")
    )
    # todo: go error if option changed to content again
    if option == "Current Content":
        display_current_content()
    elif option == "Image":
        display_image()
