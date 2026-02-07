import pandas as pd

df = pd.read_excel("online_retail_II.xlsx", sheet_name=None)

combined = pd.concat(df.values(), ignore_index=True)
combined.columns = [c.replace(" ", "_") for c in combined.columns]

combined.to_csv(
    "online_retail_pipe.csv",
    sep="|",
    index=False
)

#  LOAD DATA LOCAL INFILE 'D:\Sem 2\Forecasting\n8n-ai-agent\n8n-ai-agent\online_retail_pipe.csv'
#      INTO TABLE sales
#      FIELDS TERMINATED BY '|'
#      LINES TERMINATED BY '\n'
#      IGNORE 1 LINES;