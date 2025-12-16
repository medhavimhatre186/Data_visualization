import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/dataset.csv")

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(df["Year"], df["Sales"], marker='o', linewidth=2)

# Add labels and title
plt.title("Sales Growth Over Years", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Sales", fontsize=12)

# Add grid
plt.grid(True)

# Save the chart (for assignment / portfolio)
plt.savefig("charts/sales_growth.png")

# Show the chart
plt.show()

# Insight:
# The chart shows a steady increase in sales from 2020 to 2023,
# indicating consistent business growth over time.
