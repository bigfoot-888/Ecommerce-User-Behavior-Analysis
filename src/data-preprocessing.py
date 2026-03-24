import pandas as pd
path_oct = "./data/raw/2019-Oct.csv"
path_nov = "./data/raw/2019-Nov.csv"
chunksize = 10 ** 6
chunks_oct = []
cols = ["event_time", "event_type", "user_id", "price"]
parse_dates = ["event_time"]
with pd.read_csv(path_oct, chunksize=chunksize, usecols=cols, parse_dates=parse_dates, dtype={'event_type' : 'category'}) as reader:
    for chunk in reader:
        chunks_oct.append(chunk)
        
df_oct = pd.concat(chunks_oct, ignore_index=True)
print(df_oct.head())

chunks_nov = []

with pd.read_csv(path_nov, chunksize=chunksize, usecols=cols, parse_dates=parse_dates, dtype={'event_type' : 'category'}) as reader:
    for chunk in reader:
        chunks_nov.append(chunk)
df_nov = pd.concat(chunks_nov, ignore_index=True)
print(df_nov.head())

# Concat the two dataframes

df_total = pd.concat([df_oct, df_nov], ignore_index=True)
print(df_total.tail())

# Add week and weekday columns for the cohort analysis

df_total["week"] = df_total["event_time"].dt.isocalendar().week
df_total["weekday"] = df_total["event_time"].dt.dayofweek
print(df_total.head())

# Before processing the price column, first check and remove any rows where price is 0 or lower

df_total["price"].isna().sum()
(df_total["price"] <= 0).sum()
df_total = df_total[df_total["price"] > 0]
df_total.shape

# Bin the prices based on quartiles to divide them into "Low", "Medium", and "High"

df_total["price_range"] = pd.qcut(q=3, labels=["Low", "Medium", "High"], x=df_total["price"])
df_total.head()
df_total["price_range"].value_counts()

# Export the data

df_total.to_parquet("../data/processed/df.parquet.gzip", compression="gzip")
