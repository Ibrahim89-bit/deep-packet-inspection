import joblib
import pandas as pd
import random
import time
from datetime import datetime
import os

# Load model
model = joblib.load("model/random_forest_model.pkl")

print("=== Traffic Simulation with Logging Started ===")

protocol_map = {
    1: "TCP",
    2: "UDP",
    3: "ICMP"
}

file_path = "simulation_results.csv"

# Create file with header if not exists
if not os.path.exists(file_path):
    df = pd.DataFrame(columns=[
        "timestamp",
        "packet_size",
        "protocol",
        "prediction"
    ])
    df.to_csv(file_path, index=False)

while True:

    packet_size = random.randint(20, 2000)
    protocol = random.randint(1, 3)

    new_data = pd.DataFrame({
        "packet_size": [packet_size],
        "protocol": [protocol]
    })

    prediction = model.predict(new_data)[0]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(
        "Time:",
        timestamp,
        "| Size:",
        packet_size,
        "| Protocol:",
        protocol_map[protocol],
        "| Prediction:",
        prediction
    )

    # Save to CSV
    log_data = pd.DataFrame({
        "timestamp": [timestamp],
        "packet_size": [packet_size],
        "protocol": [protocol_map[protocol]],
        "prediction": [prediction]
    })

    log_data.to_csv(
        file_path,
        mode="a",
        header=False,
        index=False
    )

    time.sleep(2)