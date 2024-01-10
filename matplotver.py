import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#data = pd.read_csv("weight.csv",keep_default_na=False)

df = pd.read_csv("weight copy.csv")

matrix1 = df[df.columns[0]]
matrix2 = df[df.columns[1]]

list1 = matrix2.tolist()
list2 = matrix1.tolist()
 














x_axis = list2
y_axis = list1
# y_axis2 = BMI
# ax2 = plt.gca().twinx()
# ax2.set_yticks(y_axis2)
# ax2.set_ylabel("Another Y-axis data")
plt.plot(x_axis,y_axis)
# plt.plot(x_axis,y_axis2)
plt.title('Weight Loss Graph')
plt.xlabel('Date')
plt.ylabel('Weight/kg')
plt.show()