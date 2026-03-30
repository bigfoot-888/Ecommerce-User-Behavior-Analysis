import pandas as pd

def compute_cohort_data(df_total):
    df_total["first_week"] = df_total.groupby("user_id")["week"].transform("min")
    
    cohort = df_total.groupby(["first_week", "week"])["user_id"].nunique().reset_index()
    cohort.columns = ["first_week", "week", "users"]
    
    cohort["period"] = cohort["week"] - cohort["first_week"]
    
    cohort_pivot = cohort.pivot_table(index="first_week", columns="period", values="users")
    cohort_pctg = cohort_pivot.div(cohort_pivot[0], axis=0)
    
    return cohort_pctg