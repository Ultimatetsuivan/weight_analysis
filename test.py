import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#data = pd.read_csv("weight.csv",keep_default_na=False)

df = pd.read_csv("weight.csv")

matrix1 = df[df.columns[0]]
matrix2 = df[df.columns[1]]

list1 = matrix2.tolist()
list2 = matrix1.tolist()
x = pd.DataFrame(list1)
new = x.fillna(method='ffill', limit=100)
list1 = new.values.tolist()
plt.figure()
new.plot.line()
plt.savefig("graph1.png")
plt.close()

BMI = []

# for i in list1:
#     BMI.append(i/(1.64*1.64))
# print(BMI)


# while j<8:
#     sum = 0
#     for i in list1:
#         sum = sum(i)
#         count = count + 1
#         if count == 7:
#             continue
#     print(sum)
