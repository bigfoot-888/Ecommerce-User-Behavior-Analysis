import pandas as pd

def compute_cohort_data(df_total):
    weeks = df_total["week"].unique()
    first_week = df_total.groupby("user_id")["week"].min()

    df_total["first_week"] = df_total["user_id"].map(first_week)
    
    cohort_data = []
    first_week = df_total.groupby("user_id")["week"].min()
    for idx, week in enumerate(weeks):
            week_row = []
            first_time_users = df_total.loc[df_total["first_week"] == week, "user_id"].unique()
            week_row.append(len(first_time_users))
            for jdx in range(1, len(weeks) - idx):
                retention = df_total.loc[(df_total["week"] == week + jdx) & (df_total["user_id"].isin(first_time_users)), "user_id"].unique()
                week_row.append(len(retention))
            cohort_data.append(week_row)
            
    df_cohort = pd.DataFrame(cohort_data)
    df_cohort_pctg = df_cohort.div(df_cohort[0], axis=0)
    df_cohort_pctg = df_cohort_pctg 
    df_cohort_pctg.head(10)
    return df_cohort_pctg