import matplotlib.pyplot as plt
from utils import *
import seaborn as sns
import numpy as np
import os

def bivariate_plot(df, max_features=5):
    """
    Generates and saves bivariate plots for 5 numerical features.
    """
    
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    if len(numerical_cols) > max_features:
        # Take input from the user for which features to plot
        print(f"Select {max_features} features to plot (out of {len(numerical_cols)}):")
       
        # Display list of available features
        print("Available features:")
        for i, col in enumerate(numerical_cols):
            print(f"{i+1}. {col}")
        
        feature_indices = input("Enter the indices of features to plot (separated by space): ")
        feature_indices = [int(x) - 1 for x in feature_indices.split()]

        # Validate user input
        if len(feature_indices) > max_features:
            raise ValueError(f"Error: You entered {len(feature_indices)} features, but only up to {max_features} are allowed.")

        if not all(0 <= i < len(numerical_cols) for i in feature_indices):
            raise ValueError("Invalid feature indices")

        # Plot selected features
        selected_features = [numerical_cols[i] for i in feature_indices]
    else:
        # Plot all features if there are 5 or fewer
        selected_features = numerical_cols

    # configure directory
    params = read_yaml(PARAMS_FILE_PATH)
    subdir_path = os.path.join(params.save_plots, "bivariate")
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)

    # Plot selected features
    for i, col1 in enumerate(selected_features):
        for col2 in selected_features[i + 1:]:
            plt.figure(figsize=(6, 4))
            sns.scatterplot(x=df[col1], y=df[col2])
            plt.title(f'Plot: {col1} vs {col2}')
            
            plot_file = os.path.join(subdir_path, f'{col1}_vs_{col2}.png')
            plt.savefig(plot_file)
            plt.close()
