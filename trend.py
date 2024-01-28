import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Your provided data
df = pd.read_csv("csv_files/weight.csv",parse_dates=['date'])
# Reading data into a pandas DataFrame
# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['weight'], marker='o', linestyle='-', color='b')
plt.title('Weight Over Time')
plt.xlabel('Date')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()
