import pandas as pd

def process_data(df_total):
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
    
    return df_total
