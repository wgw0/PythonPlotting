import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.table import Table

# Create the data for the table
data = {
    "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "London Cost (GBP bn)": [2.3, 2.4, 2.45, 2.55, 2.6, 2.46, 2.5, 3, 3.04, 3.4, 3.5],
    "London Ridership (bn)": [1.32, 1.34, 1.35, 1.36, 1.37, 1.38, 1.39, 0.7, 0.85, 1.1, 1.3],
    "Cost per Journey (GBP)": [1.74, 1.79, 1.81, 1.87, 1.9, 1.78, 1.8, 4.29, 3.57, 3.09, 2.69],
    "Seoul Cost (GBP bn)": [1.64, 1.68, 1.7, 1.76, 1.79, 1.87, 1.95, 2.03, 2.07, 2.11, 2.15],
    "Seoul Ridership (bn)": [2.7, 2.75, 2.78, 2.8, 2.85, 2.88, 2.9, 1.5, 1.7, 2.3, 2.6],
    "Cost per Journey (GBP)": [0.61, 0.61, 0.61, 0.63, 0.63, 0.65, 0.67, 1.35, 1.22, 0.92, 0.83]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Plot the table using matplotlib
fig, ax = plt.subplots(figsize=(12, 4))  # Adjust the size for visibility
ax.axis("off")  # Turn off the axis

# Create a table from the dataframe and add it to the plot
table = Table(ax, bbox=[0, 0, 1, 1])  # Positioning the table

# Add the column headers to the table
for (i, column_name) in enumerate(df.columns):
    table.add_cell(0, i, width=1/len(df.columns), height=0.1, text=column_name, loc='center', facecolor='lightblue')

# Add the data rows to the table
for i, row in enumerate(df.values):
    for j, value in enumerate(row):
        table.add_cell(i+1, j, width=1/len(df.columns), height=0.1, text=f"{value:.2f}", loc='center', facecolor='white')

# Add the table to the axes and display the plot
ax.add_table(table)
plt.title("London Underground vs. Seoul Subway Operating Costs and Ridership (2013-2023)", fontsize=14)
plt.show()

# Optionally, export to HTML or Excel
df.to_html("transport_data_table.html", index=False)  # Save table as HTML
df.to_excel("transport_data_table.xlsx", index=False)  # Save table as Excel
