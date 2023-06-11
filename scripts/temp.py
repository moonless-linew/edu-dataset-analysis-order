import pandas as pd
df = pd.read_csv("../data/data.csv", sep=";")
print(set(df['Product']))