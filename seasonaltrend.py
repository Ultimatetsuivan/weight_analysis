import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Assuming 'date' is the column containing date information and 'weight' is the weight data
df = pd.read_csv("csv_files/weight_no_empty.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# Seasonal Decomposition
result = seasonal_decompose(df['weight'], model='additive', period=12)  # Adjust the period as needed

# Plotting
plt.figure(figsize=(12, 8))

# Original Time Series
plt.subplot(4, 1, 1)
plt.plot(df['weight'], label='Original')
plt.legend()

# Trend Component
plt.subplot(4, 1, 2)
plt.plot(result.trend, label='Trend')
plt.legend()

# Seasonal Component
plt.subplot(4, 1, 3)
plt.plot(result.seasonal, label='Seasonal')
plt.legend()

# Residual Component
plt.subplot(4, 1, 4)
plt.plot(result.resid, label='Residual')
plt.legend()

plt.tight_layout()
plt.show()
