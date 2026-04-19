import joblib
import pandas as pd
import random
import time

# Load trained model
model = joblib.load("model/random_forest_model.pkl")

print("=== Real-Time Traffic Simulation Started ===")

protocol_map = {
    1: "TCP",
    2: "UDP",
    3: "ICMP"
}

while True:

    # Generate random packet
    packet_size = random.randint(20, 2000)
    protocol = random.randint(1, 3)

    new_data = pd.DataFrame({
        "packet_size": [packet_size],
        "protocol": [protocol]
    })

    # Predict
    prediction = model.predict(new_data)[0]

    print(
        "Packet Size:",
        packet_size,
        "| Protocol:",
        protocol_map[protocol],
        "| Prediction:",
        prediction
    )

    # Wait 2 seconds
    time.sleep(2)