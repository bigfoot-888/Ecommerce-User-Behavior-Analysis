import pandas as pd

# Searches for a .env file and temporarily loads the variables
def load_data():
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

    chunks_nov = []

    with pd.read_csv(path_nov, chunksize=chunksize, usecols=cols, parse_dates=parse_dates, dtype={'event_type' : 'category'}) as reader:
        for chunk in reader:
            chunks_nov.append(chunk)
    df_nov = pd.concat(chunks_nov, ignore_index=True)
    
    df_total = pd.concat([df_oct, df_nov], ignore_index=True)
    
    return df_total