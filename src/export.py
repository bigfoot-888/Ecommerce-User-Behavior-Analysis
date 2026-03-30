def export_funnel(data):
    data.to_csv("./outputs/data/funnel_data.csv", index=False)
    
def export_segmented_funnel(data):
    data.to_csv("./outputs/data/segmented_funnel_data.csv", index=False)
    
def export_cohort(data):
    data.to_csv("./outputs/data/cohort_data.csv", index=False)