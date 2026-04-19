import argparse
from utils import (
    load_model,
    convert_protocol,
    predict_packet
)

# Load model
model = load_model()

if model is None:
    exit()

parser = argparse.ArgumentParser(
    description="DPI CLI Tool"
)

parser.add_argument(
    "--size",
    type=int,
    required=True
)

parser.add_argument(
    "--protocol",
    type=str,
    required=True
)

args = parser.parse_args()

protocol = convert_protocol(
    args.protocol
)

if protocol is None:
    exit()

prediction = predict_packet(
    model,
    args.size,
    protocol
)

print("Prediction:", prediction)