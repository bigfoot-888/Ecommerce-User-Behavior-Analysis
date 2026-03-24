import kaggle, kagglehub

from dotenv import load_dotenv

# Searches for a .env file and temporarily loads the variables
load_dotenv()

# Authenticate with Kaggle API
kaggle.api.authenticate()

# Download latest version
path = kagglehub.dataset_download("mkechinov/ecommerce-behavior-data-from-multi-category-store")

print("Path to dataset files:", path)