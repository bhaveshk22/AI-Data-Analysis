import seaborn as sns
import matplotlib.pyplot as plt
import os
from utils import *

def summarize_correlations(df):
    """
    Summarizes and plots the correlation matrix.
    """
    correlation_matrix = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    params = read_yaml(PARAMS_FILE_PATH)
    correlation_plot_file = os.path.join(params.save_plots, 'correlation_matrix.png')
    plt.savefig(correlation_plot_file)
    plt.close()
    
    return correlation_matrix