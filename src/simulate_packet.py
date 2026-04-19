import joblib
import pandas as pd

# Load saved model
model = joblib.load("model/random_forest_model.pkl")

print("=== DPI Packet Simulator ===")

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
prediction = model.predict(new_data)

print("Prediction:", prediction[0])