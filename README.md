# E-commerce Funnel & Cohort analysis 

## Overview

This project aims to analyze user behavior in an e-commerce platform using funnel and cohort analyses. 

The analysis includes:
* Funnel analysis to measure conversion rates between stages
* Segmented funnel analysis based on product price ranges
* Cohort analysis to evaluate user retention over time
* Visualization of results with Python libraries and PowerBI

The goal is to gather insights into how users progress through the customer purchase journey (view, cart, and purchase), and their engagement over time. 

---

## Technologies Used

The project was implemented in Python using the following libraries:

* pandas, numpy — data manipulation
* matplotlib, seaborn, plotly — plotting
* PowerBI — interactive dashboard visualization

Python dependencies are listed in `requirements.txt`. 

---

## Getting Started

### 1. Clone the repository

git clone https://github.com/your-username/ecommerce-funnel-cohort-analysis.git
cd ecommerce-funnel-cohort-analysis

### 2. Install dependencies

pip install -r requirements.txt

### 3. Download the dataset

The dataset is not included in the repository due to licensing restrictions. You can find it in the link below: 

https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store

There are many ways you can download it. As an example: 

1. Create a file to store environment variables
```
.env
```
2. Add your Kaggle credentiales. For example:
```
KAGGLE_USERNAME="your_username"
KAGGLE_KEY="your_key"
```
3. Run the following code:
```
load_dotenv()
kaggle.api.authenticate()
path = kagglehub.dataset_download("mkechinov/ecommerce-behavior-data-from-multi-category-store")
```
4. Place the two downloaded datasets in the project as seen below:
```
ecommerce-user-behavior-analysis/
│
├── notebooks/
│   └── user-behavior-analysis.ipynb
│
├── data/
│   ├── raw/
│   │   └── 2019-Nov.csv
│   │   └── 2019-Oct.csv
...
```
### 4. Run the project
You have two options: 
1. Open and run the notebook in notebooks/user-behavior-analysis.ipynb 
2. Go to the root of the project and run the main file:
```
python main.py
```
This will:
* Load and preprocess the data
* Compute funnel and cohort analyses
* Generate visualizations

---

## Project Structure

```
ecommerce-user-behavior-analysis/
│
├── data/
│   └── processed/
│
├── notebooks/
│   └── user-behavior-analysis.ipynb
│
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── funnel.py
│   ├── cohort.py
│   └── visualization.py
│
├── images/
│   ├── ...
│   └── ...
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Analysis Overview

1. Data Loading

Loading and combining multiple monthly datasets, using chunked reading for efficiency.

2. Data Preprocessing
* Timestamp processing (week extraction)
* Data cleaning (removal of invalid values)
* Price segmentation into ranges (low, medium, high)
  
3. Funnel Analysis

First, a strict funnel was implemented with three stages:

1. **View**: a customer views a product
2. **Cart**: a customer places a product in their cart
3. **Purchase**: a customer buys a product

It is important to note that users are not obligated to follow this specific order; they could purchase a product without viewing it, or place one in their cart and buy a different one. To keep the analysis clean, only users that followed all three stages in order were considered.

4. Segmented Funnel Analysis

To give further insights on the funnel analysis, the previous funnel setup was expanded to use a price-based segmentation, with the following segments:

1. **Low**
2. **Medium**
3. **High**

This allows us to see how user behavior and conversion rates may vary based on product prices. 

5. Cohort Analysis

Users were grouped into cohorts based on their first interaction week.

**Retention** is measured as the percentage of users who return in subsequent weeks, regardless of whether they view, cart, or purchase a product. 

## Key Insights

** Significant drop after first interaction
A large proportion of users do not return after their initial visit.
Conversion varies by price range
Lower-priced products tend to drive higher initial engagement, while higher-priced products may show stronger purchase intent.
Retention stabilizes after initial drop
Users who return after the first week are more likely to remain engaged over time.
Presence of a core user base
A subset of users consistently interacts with the platform, indicating strong engagement among retained users.

- **Significant drop after first interaction.**  
A large proportion of users do not return after their initial visit.

- **Conversion varies slightly by price range**  
Medium-priced products show the highest conversion rates, with high-priced products being slightly ahead of lower-priced ones. 

- **Retention stabilizes after initial drop**  
Users who return after the first week are very likely to remain engaged and keep coming back to the platform over time. These users consistently interact with the platform, indicating good engagement among users and the presence strong fidelity systems.

## Visualizations

...

## PowerBI Dashboard

...

---

## License

This repository is licensed under the **MIT License**.

Note that the dataset used in this project is provided by Kaggle and is not redistributed in this repository. To use the same dataset, you have to download it yourself directly from Kaggle. 

---

## Author

David Xu Hu  
BSc Software Engineering — Universidad Complutense de Madrid

GitHub: https://github.com/bigfoot-888
LinkedIn: www.linkedin.com/in/david-xu-hu-bb8abb350
