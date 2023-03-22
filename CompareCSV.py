import pandas as pd

# Load the two CSV files into memory as pandas DataFrames
df1 = pd.read_csv("file1.csv")
df2 = pd.read_csv("file2.csv")

# Compare the two DataFrames
compare = df1.compare(df2)

# Create a new DataFrame to store the rows that are different
diff = pd.DataFrame(columns=df1.columns)

# Iterate through the results of the compare method and add the rows that are different to the new DataFrame
for row in compare.index:
    if compare.loc[row].any():
        diff = pd.concat([diff, df2.loc[row].to_frame().transpose()])

# Save the new DataFrame to a new CSV file
diff.to_csv("different_rows.csv", index=False)