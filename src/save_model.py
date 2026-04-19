import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

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

# Save model
with open("model/dpi_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully")