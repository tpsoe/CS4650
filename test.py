from pandas import Series, DataFrame
import pandas as pd
import numpy as np


df = pd.read_csv("Salaries.csv")
# print(df.tail(10))
# print(df.head(100))
# print(df['salary'].dtype)
# print(df.dtypes)
# print(df.axes)
# print(df.std())

# m = df.head(50)
# print(m.mean())

print(df.std())
