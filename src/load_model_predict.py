import pickle

# Load saved model
with open("model/dpi_model.pkl", "rb") as f:
    model = pickle.load(f)

# User input
packet_size = int(input("Enter Packet Size: "))
protocol = input("Enter Protocol (TCP/UDP/ICMP): ")

# Convert protocol to number
protocol_map = {
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
}

protocol_number = protocol_map.get(protocol.upper())

# Prediction
prediction = model.predict([[packet_size, protocol_number]])

print("Prediction:", prediction[0])