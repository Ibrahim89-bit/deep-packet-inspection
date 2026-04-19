import joblib
import pandas as pd

# Protocol mapping
PROTOCOL_MAP = {
    "TCP": 1,
    "UDP": 2,
    "ICMP": 3
}

def load_model():

    try:
        model = joblib.load(
            "model/random_forest_model.pkl"
        )
        return model

    except FileNotFoundError:

        print(
            "Error: Model file not found."
        )

        return None


def convert_protocol(protocol_name):

    protocol_name = protocol_name.upper()

    if protocol_name not in PROTOCOL_MAP:

        print(
            "Invalid protocol."
        )

        return None

    return PROTOCOL_MAP[protocol_name]


def predict_packet(
    model,
    packet_size,
    protocol
):

    data = pd.DataFrame({

        "packet_size": [packet_size],
        "protocol": [protocol]

    })

    prediction = model.predict(
        data
    )[0]

    return prediction