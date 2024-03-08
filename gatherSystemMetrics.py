import psutil
import time
import subprocess
import re

def monitor_system(interval=1, total_run_time=60, log_file="system_monitor.log", interface='wlan0'):

    start_time = time.time()

    with open(log_file, "a") as f:
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= total_run_time:
                f.write("Completed monitoring. Exiting script.\n")
                break

            # CPU times
            cpu_times = psutil.cpu_times()
            f.write(f"CPU Times: {cpu_times}\n")

            # CPU percent
            cpu_percent = psutil.cpu_percent(interval)
            f.write(f"CPU Percent: {cpu_percent}%\n")

            # Virtual Memory
            virtual_memory = psutil.virtual_memory()
            f.write(f"Virtual Memory: {virtual_memory}\n")

            # WiFi Signal Strength
            wifi_signal = get_wifi_signal_strength(interface)
            f.write(f"WiFi Signal Strength on {interface}: {wifi_signal}\n")

            f.flush()
            time.sleep(interval)

def get_wifi_signal_strength(interface='wlan0'):
    try:
        iwconfig_output = subprocess.check_output(['iwconfig', interface], text=True)
        
        match = re.search("Quality=([^ ]+)", iwconfig_output)
        if match:
            return match.group(1)
        else:
            return "Signal quality not found"
    
    except subprocess.CalledProcessError:
        return "Failed to execute iwconfig"

if __name__ == "__main__":
    monitor_system(interval=5, total_run_time=30, log_file="system_monitor.log")  # Adjust interval, total run time, and log file path as needed
