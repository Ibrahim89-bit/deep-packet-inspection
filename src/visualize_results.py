import pandas as pd
import matplotlib.pyplot as plt

print("Loading data...")

# Read CSV file
data = pd.read_csv("simulation_results.csv")

print("Data loaded successfully")

# Count predictions
counts = data["prediction"].value_counts()

print("Prediction Counts:")
print(counts)

# Create bar chart
plt.bar(counts.index, counts.values)

plt.title("Attack vs Normal Traffic")
plt.xlabel("Prediction")
plt.ylabel("Count")

# Save graph as image
plt.savefig("traffic_graph.png")

print("Graph saved as traffic_graph.png")

# Show graph
plt.show()