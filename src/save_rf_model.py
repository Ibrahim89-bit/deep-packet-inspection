import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("data/traffic.csv")

# Convert protocol to numbers
data["protocol"] = data["protocol"].map({
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
})

# Features and labels
X = data[["packet_size", "protocol"]]
y = data["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Random Forest model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model/random_forest_model.pkl")

print("Random Forest model saved successfully")