import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("data/traffic.csv")

# Convert protocol to numbers
data["protocol"] = data["protocol"].map({
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
})

# Features and label
X = data[["packet_size", "protocol"]]
y = data["label"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# User input
packet_size = int(input("Enter Packet Size: "))
protocol = input("Enter Protocol (TCP/UDP/ICMP): ")

# Convert protocol
protocol_map = {
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
}

protocol_number = protocol_map.get(protocol.upper())

# Prediction
prediction = model.predict([[packet_size, protocol_number]])

print("Prediction:", prediction[0])