import matplotlib.pyplot as plt

# Good Version, demonstrates COST to Usage ratios (TfL losing out)
# Data for the London Underground and Seoul Subway (in GBP billions and billions of passengers)
years = list(range(2013, 2024))
london_costs_gbp = [2.30, 2.40, 2.45, 2.55, 2.60, 2.46, 2.50, 3.00, 3.04, 3.40, 3.50]
seoul_costs_gbp = [1.64, 1.68, 1.70, 1.76, 1.79, 1.87, 1.95, 2.03, 2.07, 2.11, 2.15]
london_ridership = [1.32, 1.34, 1.35, 1.36, 1.37, 1.38, 1.39, 0.70, 0.85, 1.10, 1.30]
seoul_ridership = [2.70, 2.75, 2.78, 2.80, 2.85, 2.88, 2.90, 1.50, 1.70, 2.30, 2.60]

# Create a figure with two y-axes for cost and ridership
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot costs on the first y-axis
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Operating Costs (GBP billions)", color="tab:blue", fontsize=12)
ax1.plot(years, london_costs_gbp, label="London Underground Costs", marker="o", color="tab:blue")
ax1.plot(years, seoul_costs_gbp, label="Seoul Subway Costs", marker="o", linestyle="--", color="tab:cyan")
ax1.tick_params(axis="y", labelcolor="tab:blue")
ax1.legend(loc="upper left", fontsize=10)

# Create a second y-axis for ridership
ax2 = ax1.twinx()
ax2.set_ylabel("Ridership (Billions of Passengers)", color="tab:green", fontsize=12)
ax2.plot(years, london_ridership, label="London Underground Ridership", marker="s", color="tab:green")
ax2.plot(years, seoul_ridership, label="Seoul Subway Ridership", marker="s", linestyle="--", color="tab:olive")
ax2.tick_params(axis="y", labelcolor="tab:green")
ax2.legend(loc="upper right", fontsize=10)

# Add a title and grid for clarity
plt.title("Operating Costs and Ridership: London Underground vs. Seoul Subway (2013–2023)", fontsize=14)
ax1.grid(axis="x", linestyle="--", alpha=0.7)

# Adjust layout and show the plot
fig.tight_layout()
plt.show()
