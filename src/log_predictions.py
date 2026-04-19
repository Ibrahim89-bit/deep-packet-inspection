import joblib
import pandas as pd
from datetime import datetime

# Load saved model
model = joblib.load("model/random_forest_model.pkl")

print("=== DPI Packet Logger ===")

# Take user input
packet_size = int(input("Enter packet size: "))

protocol_name = input("Enter protocol (TCP/UDP/ICMP): ")

# Convert protocol to number
protocol_map = {
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
}

protocol = protocol_map.get(protocol_name.upper())

# Create DataFrame
new_data = pd.DataFrame({
    "packet_size": [packet_size],
    "protocol": [protocol]
})

# Prediction
prediction = model.predict(new_data)[0]

print("Prediction:", prediction)

# Get current time
now = datetime.now()

timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Save to log file
log_entry = (
    f"{timestamp}, "
    f"Packet Size: {packet_size}, "
    f"Protocol: {protocol_name}, "
    f"Prediction: {prediction}\n"
)

with open("prediction_logs.txt", "a") as file:
    file.write(log_entry)

print("Prediction saved to log file")