import pandas as pd
import numpy as np
data = pd.read_csv("weight.csv",keep_default_na=False)
data.date()
#data.plot(x = 'date',y = 'weight')