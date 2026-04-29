import streamlit as st
import joblib
import plotly.express as px
import pandas as pd
import os

# Page settings
st.set_page_config(
    page_title="AI Deep Packet Inspection",
    page_icon="🛡️"
)

st.title("AI-Based Deep Packet Inspection System")

# Load model safely (deployment friendly)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "models",
    "random_forest_model.pkl"
)

model = joblib.load(model_path)

# User input
size = st.number_input(
    "Packet Size",
    min_value=0,
    max_value=5000,
    value=100
)

protocol = st.selectbox(
    "Protocol",
    ["TCP", "UDP", "ICMP"]
)

# IMPORTANT — mapping must match training
protocol_map = {
    "TCP": 0,
    "UDP": 1,
    "ICMP": 2
}

# Store history
if "history" not in st.session_state:
    st.session_state.history = []

# Prediction button
if st.button("Predict"):

    prediction = model.predict([
        [size, protocol_map[protocol]]
    ])

    # Debug line (optional)
    st.write("Prediction value:", prediction)

    if prediction[0] == 0:
        result = "Normal"
        st.success("Normal Traffic Detected")
    else:
        result = "Suspicious"
        st.error("Suspicious Traffic Detected")

    # Save history
    st.session_state.history.append({
        "Protocol": protocol,
        "Result": result
    })

# Show metrics
if len(st.session_state.history) > 0:

    total = len(st.session_state.history)

    normal_count = sum(
        1 for x in st.session_state.history
        if x["Result"] == "Normal"
    )

    suspicious_count = sum(
        1 for x in st.session_state.history
        if x["Result"] == "Suspicious"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total", total)
    col2.metric("Normal", normal_count)
    col3.metric("Suspicious", suspicious_count)

    # Create DataFrame
    df = pd.DataFrame(st.session_state.history)

    count_df = (
        df["Result"]
        .value_counts()
        .reset_index()
    )

    count_df.columns = [
        "Result",
        "Count"
    ]

    # Graph
    fig = px.bar(
        count_df,
        x="Result",
        y="Count",
        title="Traffic Prediction Summary"
    )

    st.plotly_chart(fig)
    