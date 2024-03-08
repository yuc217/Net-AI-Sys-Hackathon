import psutil
import time
import subprocess
import re
import csv

def monitor_system(interval=1, total_run_time=60, csv_file="system_monitor.csv", interface='wlan0'):
    start_time = time.time()
    
    with open(csv_file, mode="w", newline='') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(["Time", "CPU Percent", "Virtual Memory", "WiFi Signal Strength"])

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= total_run_time:
                break

            # CPU percent
            cpu_percent = psutil.cpu_percent(interval)

            # Virtual Memory
            virtual_memory = psutil.virtual_memory().percent  # Assuming you want the percentage

            # WiFi Signal Strength
            wifi_signal = get_wifi_signal_strength(interface)

            # Write data row
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), cpu_percent, virtual_memory, wifi_signal])

            time.sleep(interval)

def get_wifi_signal_strength(interface='wlan0'):
    try:
        iwconfig_output = subprocess.check_output(['iwconfig', interface], text=True)
        match = re.search("Quality=([^ ]+)", iwconfig_output)
        return match.group(1) if match else "Signal quality not found"
    except subprocess.CalledProcessError:
        return "Failed to execute iwconfig"

if __name__ == "__main__":
    monitor_system(interval=5, total_run_time=30, csv_file="system_monitor.csv")  # Adjust interval, total run time, and csv file path as needed
