from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pandas as pd
import numpy as np

df = pd.read_csv('corona2.csv')

result = np.where(df['date'] == '2020-03-29', df['cases'], 0).sum()
print(result)