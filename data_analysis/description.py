from utils import *
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_dataset(df):
    # Check for missing values
    missing_values = df.isnull().sum().sum()
    missing_values_percentage = (missing_values / len(df)) * 100
    
    # Check for duplicate rows
    duplicate_rows = df.duplicated().sum().sum()
    duplicate_rows_percentage = (duplicate_rows / len(df)) * 100
    
    statistics = {"overall": {"missing_values" : missing_values,
                              "missing_values_percentage" : round(missing_values_percentage,2),
                              "duplicate_rows" : duplicate_rows,
                              "duplicate_rows_percentage" : round(duplicate_rows_percentage,2)}}
    
    # Distribution plot for individual features
    for column in df.columns:

        missing_values = df[column].isnull().sum()
        missing_values_percentage = (missing_values / len(df[column])) * 100

        distinct_values = df[column].nunique()
        distinct_values_percentage = (distinct_values / len(df[column])) * 100

        statistics[column] = {"missing_values": missing_values,
                                "missing_values_percentage" : round(missing_values_percentage,2),
                                "distinct_values": distinct_values,
                                "distinct_values_percentage": round(distinct_values_percentage,2)}

        numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
        if column in numerical_columns:
            plt.figure(figsize=(6, 4))
            sns.histplot(df[column])
            plt.title(f"Distribution of {column}")
            params = read_yaml(PARAMS_FILE_PATH)
            output_file = os.path.join(params.save_plots, f"{column}-distribution.png")
            plt.savefig(output_file)
            plt.close()
    
    # basic description of the dataset
    description = df.describe()
    
    return statistics, description


