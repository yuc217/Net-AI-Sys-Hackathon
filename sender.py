import subprocess
import socket
import time

# read lines from the system_monitor.log file
def get_latest_input_text():
    with open("system_monitor.log", "r") as f:
        lines = f.readlines()
        input_text = "".join(lines[-3:])
    return input_text

# stress the system
def stress_test():
    cpu_count = 4  
    stress_duration = 100 #seconds
    subprocess.run(['stress', '--cpu', str(cpu_count), '--timeout', str(stress_duration)])

# launch the TinyLlama model
def launch_model_subprocess(prompt):
    with open("report.txt", 'w') as output_file_handle:
        model_process = subprocess.run(
        [
            "sh",
            "/home/device3/TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile",
            "-ngl", "9999",
            "-t", "0.8",
            "-p", prompt
        ],
        stdin=subprocess.PIPE,
        stdout=output_file_handle,
        text=True

    )
        return model_process
        
    
# TCP connection and data transfer
def send_receive_data(output, host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(output.encode())
    received_data = client_socket.recv(1024).decode()
    client_socket.close()
    return received_data

if __name__ == "__main__":
    host = '192.168.50.61'
    port = 60000
    prompt = ""

    while True:
        input_text = get_latest_input_text()
        prompt = f"[INST]Evaluate system load and device status monitoring from this data: {input_text} [/INST]"
        # uncomment this for the stress condition
        # stress_test()
        model_process = launch_model_subprocess(prompt)

        # check if model subprocess executed successfully
        if model_process.returncode != 0:
            message = 'Failed to generate LLM report due to stress.'
            send_receive_data(message, host, port)
        else:
            with open("report.txt", "r") as f:
                output = f.read()
            print("Generated Text:")
            print(output)
            received_data = send_receive_data(output, host, port)
            print("Received data:")
            print(received_data)
            time.sleep(10)  

