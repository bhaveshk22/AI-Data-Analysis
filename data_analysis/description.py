from utils import *
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_dataset(df):
    # shape of the dataset
    shape = df.shape

    # Check for missing values
    missing_values = df.isnull().sum().sum()
    missing_values_percentage = (missing_values / len(df)) * 100
    
    # Check for duplicate rows
    duplicate_rows = df.duplicated().sum().sum()
    duplicate_rows_percentage = (duplicate_rows / len(df)) * 100
    
    statistics = {"overall": {"shape" : shape,
                              "missing_values" : missing_values,
                              "missing_values_percentage" : round(missing_values_percentage,2),
                              "duplicate_rows" : duplicate_rows,
                              "duplicate_rows_percentage" : round(duplicate_rows_percentage,2)}}
    
    # Configure directory
    params = read_yaml(PARAMS_FILE_PATH)
    subdir_path = os.path.join(params.save_plots, "distribution")
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)

    # numerical cols
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

    # Distribution plot for individual features
    for column in df.columns:

        missing_values = df[column].isnull().sum()
        missing_values_percentage = (missing_values / len(df[column])) * 100

        distinct_values = df[column].nunique()
        distinct_values_percentage = (distinct_values / len(df[column])) * 100


        if column in numerical_columns:
            # detecting outliers
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
            
            outlier_count = outliers.shape[0]
            outlier_percentage = (outlier_count / df.shape[0]) * 100

            #plotting the distribution plot
            plt.figure(figsize=(6, 4))
            sns.histplot(df[column])
            plt.title(f"Distribution of {column}")
            
            output_file = os.path.join(subdir_path, f"{column}.png")
            plt.savefig(output_file)
            plt.close()


        # storing results
        statistics[column] = {"missing_values": missing_values,
                              "missing_values_percentage" : round(missing_values_percentage,2),
                              "distinct_values": distinct_values,
                              "distinct_values_percentage": round(distinct_values_percentage,2),
                              "outliers": outlier_count,
                              "outliers_percentage": round(outlier_percentage,2)}
    # basic description of the dataset
    description = df.describe().to_dict()
    
    return statistics, description


