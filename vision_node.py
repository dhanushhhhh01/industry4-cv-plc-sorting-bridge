import cv2
import numpy as np
import paho.mqtt.client as mqtt

# --- Configuration ---
MQTT_BROKER = "localhost" # Or your PLC IP
MQTT_TOPIC = "factory/sorter/color"

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define "Industry Green" (Change these thresholds for your specific parts)
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    
    mask = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Check if a significant object is detected
    if np.sum(green_mask) > 500000: # Pixel threshold
        return "GREEN"
    return "NONE"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    color = detect_color(frame)
    
    if color != "NONE":
        print(f"Object Detected: {color}")
        client.publish(MQTT_TOPIC, color)
    
    cv2.imshow('Industry 4.0 Vision Node', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
