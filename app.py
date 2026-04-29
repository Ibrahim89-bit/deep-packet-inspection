import streamlit as st
import joblib
import plotly.express as px
import pandas as pd

st.title("AI-Based Deep Packet Inspection")

# Load model
model = joblib.load("models/random_forest_model.pkl")

# User input
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

# Store results for graph
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Predict"):

    prediction = model.predict(
        [[size, protocol_map[protocol]]]
    )

    if prediction[0] == 0:
        result = "Normal"
        st.success("Normal Traffic")
    else:
        result = "Suspicious"
        st.error("Suspicious Traffic")

    # Save history
    st.session_state.history.append({
        "Protocol": protocol,
        "Result": result
    })

# ----- GRAPH SECTION -----

if len(st.session_state.history) > 0:

    df = pd.DataFrame(st.session_state.history)

    count_df = df["Result"].value_counts().reset_index()
    count_df.columns = ["Result", "Count"]

    fig = px.bar(
        count_df,
        x="Result",
        y="Count",
        title="Traffic Prediction Summary"
    )

    # IMPORTANT LINE (graph display)
    st.plotly_chart(fig)