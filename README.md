# Industry 4.0 Sorting Bridge

## Overview
This project simulates a high-speed industrial conveyor sorting line. It uses **OpenCV** for visual inspection and **MQTT** to bridge the gap between high-level AI logic and low-level PLC execution.

## Technical Stack
*   **Vision:** OpenCV (HSV Masking)
*   **Messaging:** MQTT (Mosquitto)
*   **Control Logic:** Python / Simulated PLC
*   **Hardware (Optional):** Arduino Opta / Raspberry Pi

## Architecture
1. **Vision Node:** Captures frames and analyzes color values.
2. **Broker:** Handles asynchronous messaging between Python and the Controller.
3. **Control Node:** Triggers hardware solenoids based on color identification.
