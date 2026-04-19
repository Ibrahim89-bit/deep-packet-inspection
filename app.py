import streamlit as st
import joblib

st.title("AI-Based Deep Packet Inspection")

# Load model
model = joblib.load("model/random_forest_model.pkl")

size = st.number_input("Packet Size", min_value=0)

protocol = st.selectbox(
    "Protocol",
    ["TCP", "UDP", "ICMP"]
)

protocol_map = {
    "TCP": 0,
    "UDP": 1,
    "ICMP": 2
}

if st.button("Predict"):
    prediction = model.predict(
        [[size, protocol_map[protocol]]]
    )

    if prediction[0] == 0:
        st.success("Normal Traffic")
    else:
        st.error("Suspicious Traffic")