import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#data = pd.read_csv("weight.csv",keep_default_na=False)

df = pd.read_csv("csv_files/weight.csv")

df['date'] = pd.to_datetime(df['date'])
monthly_avg = df.set_index('date').resample('M').mean()

weekly_avg = df.set_index('date').resample('W').mean()

print(monthly_avg)

print(weekly_avg)

# plt.figure(figsize=(10, 6))
# plt.plot(monthly_avg.index, monthly_avg['weight'], marker='o', linestyle='-')
# plt.title('Monthly Average Weight')
# plt.xlabel('Month')
# plt.ylabel('Average Weight')
# plt.grid(True)
# plt.savefig('graphs/monthly.png')
# plt.show()

plt.figure(figsize=(10, 6))
plt.plot(weekly_avg.index, weekly_avg['weight'], marker='o', linestyle='-')
plt.title('Weekly Average Weight')
plt.xlabel('Date')
plt.ylabel('Average Weight')
plt.grid(True)
plt.savefig('graphs/weekly.png')
plt.show()