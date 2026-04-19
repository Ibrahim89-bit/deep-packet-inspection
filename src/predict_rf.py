import joblib
import pandas as pd

# Load saved model
model = joblib.load("model/random_forest_model.pkl")

print("Model loaded successfully")

# New packet data
new_data = pd.DataFrame({
    "packet_size": [1600],
    "protocol": [1]   # TCP = 1, UDP = 2, ICMP = 3
})

# Prediction
prediction = model.predict(new_data)

print("Prediction:", prediction[0])