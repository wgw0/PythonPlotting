import matplotlib.pyplot as plt

# Data for the London Underground and Seoul Subway (in GBP billions)
years = list(range(2013, 2024))
london_costs_gbp = [2.30, 2.40, 2.45, 2.55, 2.60, 2.46, 2.50, 3.00, 3.04, 3.40, 3.50]
seoul_costs_gbp = [1.64, 1.68, 1.70, 1.76, 1.79, 1.87, 1.95, 2.03, 2.07, 2.11, 2.15]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(years, london_costs_gbp, label="London Underground", marker="o")
plt.plot(years, seoul_costs_gbp, label="Seoul Subway", marker="o", linestyle="--")

# Titles and labels
plt.title("Operating Costs of London Underground and Seoul Subway (2013–2023)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Operating Costs (GBP billions)", fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the graph
plt.tight_layout()
plt.show()
