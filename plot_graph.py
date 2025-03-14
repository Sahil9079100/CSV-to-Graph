from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import DatetimeTickFormatter
import pandas as pd
import random

#sail and rishi

curdoc().theme = "dark_minimal"

# Read CSV
data = pd.read_csv('2024-01-25 11.03.29 2X18650_PcUSBOnly(3).csv', header=None)

# Convert time column to timedelta
time_column = pd.to_timedelta(data[2], errors='coerce')

# User input
selected_columns = input("Enter the column numbers (comma-separated): ")
selected_columns = [int(col) - 1 for col in selected_columns.split(',')]

output_file("plot.html")

# Generate random colors for each selected column
colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(len(selected_columns))]

p = figure(title="Data vs Time", x_axis_label='Time', y_axis_label='Value', width=1915, height=990,
           background_fill_color="#141414")

# Plot selected columns v/s time with random colors
for col, color in zip(selected_columns, colors):
    p.line(time_column, data[col], legend_label=f'Column {col + 1}', line_width=2, line_color=color)

p.xaxis.formatter = DatetimeTickFormatter(
    milliseconds=["%H:%M:%S.%f"]
)

# Change grid lines color to white
p.grid.grid_line_color = "#FFFFFF"

# Show legend
p.legend.location = "top_left"

# Show the plot
show(p)
