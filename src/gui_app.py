import tkinter as tk
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model/random_forest_model.pkl")

# Function to predict
def predict_packet():

    packet_size = int(packet_entry.get())
    protocol_name = protocol_entry.get().upper()

    protocol_map = {
        "TCP": 1,
        "UDP": 2,
        "ICMP": 3
    }

    protocol = protocol_map.get(protocol_name)

    new_data = pd.DataFrame({
        "packet_size": [packet_size],
        "protocol": [protocol]
    })

    prediction = model.predict(new_data)[0]

    result_label.config(
        text=f"Result: {prediction}"
    )


# Create window
window = tk.Tk()
window.title("DPI Packet Predictor")
window.geometry("350x250")

# Packet size input
tk.Label(
    window,
    text="Packet Size:"
).pack()

packet_entry = tk.Entry(window)
packet_entry.pack()

# Protocol input
tk.Label(
    window,
    text="Protocol (TCP/UDP/ICMP):"
).pack()

protocol_entry = tk.Entry(window)
protocol_entry.pack()

# Predict button
tk.Button(
    window,
    text="Predict",
    command=predict_packet
).pack(pady=10)

# Result label
result_label = tk.Label(
    window,
    text="Result will appear here"
)

result_label.pack()

# Run app
window.mainloop()