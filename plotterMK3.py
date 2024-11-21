import matplotlib.pyplot as plt
import numpy as np

# Compares cost per journey data, again TfL loses out...
# Data for visualisation
years = np.array(range(2013, 2024))
london_costs_gbp = [2.30, 2.40, 2.45, 2.55, 2.60, 2.46, 2.50, 3.00, 3.04, 3.40, 3.50]
seoul_costs_gbp = [1.64, 1.68, 1.70, 1.76, 1.79, 1.87, 1.95, 2.03, 2.07, 2.11, 2.15]
london_ridership = [1.32, 1.34, 1.35, 1.36, 1.37, 1.38, 1.39, 0.70, 0.85, 1.10, 1.30]
seoul_ridership = [2.70, 2.75, 2.78, 2.80, 2.85, 2.88, 2.90, 1.50, 1.70, 2.30, 2.60]

# Derived metric: Cost per passenger journey
london_cost_per_journey = [c / r if r != 0 else 0 for c, r in zip(london_costs_gbp, london_ridership)]
seoul_cost_per_journey = [c / r if r != 0 else 0 for c, r in zip(seoul_costs_gbp, seoul_ridership)]

# Create a dual-bar chart for Cost per Journey
x = np.arange(len(years))  # Bar positions
bar_width = 0.35

fig, ax = plt.subplots(figsize=(14, 7))

# Bar plots for cost per journey
bars1 = ax.bar(x - bar_width/2, london_cost_per_journey, bar_width, label="London Underground", color="tab:blue")
bars2 = ax.bar(x + bar_width/2, seoul_cost_per_journey, bar_width, label="Seoul Subway", color="tab:green")

# Annotating the bars
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f"{bar.get_height():.2f}", 
            ha='center', va='bottom', fontsize=9, color="tab:blue")
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f"{bar.get_height():.2f}", 
            ha='center', va='bottom', fontsize=9, color="tab:green")

# Add labels, title, and legend
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Cost per Journey (GBP)", fontsize=12)
ax.set_title("Cost Efficiency: Operating Cost per Journey (2013–2023)", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=10, rotation=45)
ax.legend(fontsize=10)
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Adjust layout and display
fig.tight_layout()
plt.show()
