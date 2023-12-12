import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#data = pd.read_csv("weight.csv",keep_default_na=False)

df = pd.read_csv("weight.csv")
matrix2 = df[df.columns[0]]
matrix1 = df[df.columns[1]]
list2 = matrix2.tolist()
list1 = matrix1.tolist()

x_axis = list2
y_axis = list1
plt.plot(x_axis,y_axis)
plt.title('title name')
plt.xlabel('x_axis name')
plt.ylabel('y_axis name')
plt.show()