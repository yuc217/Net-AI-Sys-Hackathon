import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('system_monitor.csv')

# Convert 'Time' column to datetime if it's not already in that format
df['Time'] = pd.to_datetime(df['Time'])

# Plotting each metric in separate subplots
plt.figure(figsize=(15, 10))

# Plotting CPU Percent
plt.subplot(3, 1, 1)
plt.plot(df['Time'], df['CPU Percent'], label='CPU Usage', color='blue')
plt.xlabel('Time')
plt.ylabel('CPU Usage (%)')
plt.title('CPU Usage Over Time')
plt.xticks(rotation=45)
plt.legend()

# Plotting Virtual Memory
plt.subplot(3, 1, 2)
plt.plot(df['Time'], df['Virtual Memory'], label='Virtual Memory', color='green')
plt.xlabel('Time')
plt.ylabel('Virtual Memory (%)')
plt.title('Virtual Memory Usage Over Time')
plt.xticks(rotation=45)
plt.legend()

# Plotting WiFi Signal Strength
plt.subplot(3, 1, 3)
plt.plot(df['Time'], df['WiFi Signal Strength'], label='WiFi Signal Strength', color='red')
plt.xlabel('Time')
plt.ylabel('WiFi Signal Strength')
plt.title('WiFi Signal Strength Over Time')
plt.xticks(rotation=45)
plt.legend()

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
