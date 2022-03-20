import csv
import pandas as pd

df = pd.read_csv('final.csv')
print(df.shape)

del df["Unnamed: 5"]
del df["Name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]

df = df.rename({
    "Unnamed: 0": "Sr. no."
},
axis="columns")

print(df.shape)
print(list(df))

df.to_csv("Main.csv")