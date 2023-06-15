import pandas as pd

df = pd.read_csv("./raw/seriearaw.csv").drop(columns="RowNo")

df = df.groupby(["Year", "Winner"]).count()["Result"]

df.to_csv("./process/seriesProcessed.csv")

print(df.head())
