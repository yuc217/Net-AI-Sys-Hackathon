# Networked AI Systems Hackathon Challenge README

This repository contains the code for the lecture Networked AI Systems Hackathon Challenge. The project aims to implement a simple orchestration system to manage, monitor, and report network traffic data and system health across a cluster of Raspberry Pi (RPi) devices.

## Project Files

- `gatherSystemMetrics.py`: A script to gather system metrics such as CPU times, CPU percent, virtual memory, and WiFi signal strength.
- `metricsCSV.py`: A script to monitor system metrics and write them to a CSV file.
- `sender.py`: A script to send and receive data between RPi devices and the central server.
- `central_server.py`: A central node server to display real-time data received from RPi devices and visualizations.
- `visualizations.py`: A module containing functions to generate visualizations based on gathered data.


## Project Setup

1. Install the required packages:
   ```
   pip install psutil subprocess socket streamlit
   ```
2. Set up a cluster of three Raspberry Pi devices with the given scripts.
3. Run `gatherSystemMetrics.py` and `metricsCSV.py` on each RPi device to gather system metrics.
4. Run `sender.py` on each RPi device to send gathered data to the central server.
5. Run `central_server.py` on the central server to display real-time data received from RPi devices and visualize gathered data.
