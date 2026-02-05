import pandas as pd

df = pd.read_excel("online_retail_II.xlsx", sheet_name=None)

combined = pd.concat(df.values(), ignore_index=True)
combined.columns = [c.replace(" ", "_") for c in combined.columns]

combined.to_csv(
    "online_retail_pipe.csv",
    sep="|",
    index=False
)
