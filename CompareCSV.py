import pandas as pd
import numpy as np

# load file1
df1 = pd.read_csv('file1.csv')

# load file2
df2 = pd.read_csv('file2.csv')

# compare values of two files
if df1.equals(df2):
    print("Values are the same")
else:
    # find diferens in two files
    diff = np.where(df1 != df2)
    print(f"Deferenses are find {len(diff[0])} field:")
    for row, col in zip(diff[0], diff[1]):
        print(f"Row {row}, column {col}: {df1.iloc[row, col]} != {df2.iloc[row, col]}")