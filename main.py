
from src.data_ingestion import load_data
from src.data_preprocessing import process_data

from src.cohort import compute_cohort_data
from src.funnel import compute_basic_funnel
from src.funnel import compute_price_segmented_funnel

from src.visualization import visualize_cohort
from src.visualization import visualize_funnel
from src.visualization import visualize_price_segmented_funnel

from src.export import export_funnel
from src.export import export_segmented_funnel
from src.export import export_cohort

# Load and preprocess the data
data = load_data()
processed_data = process_data(data)

# Funnel analysis
funnel = compute_basic_funnel(processed_data)
funnel_price = compute_price_segmented_funnel(processed_data)

# Cohort analysis
cohort = compute_cohort_data(processed_data)

# Visualizations
fig_funnel = visualize_funnel(funnel)
fig_price = visualize_price_segmented_funnel(funnel_price)
fig_cohort = visualize_cohort(cohort)

# Show plots
fig_funnel.show()
fig_price.show()
fig_cohort.show()

# Export the data

export_funnel(funnel)
export_segmented_funnel(funnel_price)
export_cohort(cohort)
