import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("csv_files/weight.csv")

q = df['weight'].max()
p = df['weight'].min()
m = df['weight'].median()
a = df['weight'].mean()


print("Your maximum weight in last 2 year is ",q,"kg")
print("Your minimum weight in last 2 year is ",p,"kg")
print("Your median weight in last 2 year is ",m,"kg")
print("Your average weight in last 2 year is ",a,"kg")