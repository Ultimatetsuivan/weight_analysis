import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv_files/weight_no_empty.csv")

matrix1 = df[df.columns[0]]
matrix2 = df[df.columns[1]]

list1 = matrix2.tolist()
list2 = matrix1.tolist()
x_axis = list2
y_axis = list1

plt.plot(x_axis, y_axis)
plt.title('Weight Loss Graph')
plt.xlabel('Date')
plt.ylabel('Weight/kg')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45, ha="right")
plt.axhline(y=75, color='red', linestyle='--', label='Target Weight')

plt.show()
