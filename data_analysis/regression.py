import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *
import os
from sklearn.linear_model import LinearRegression


def regression_trend(df):
    """
    Uses Linear Regression to identify trends in the data.
    """
    trends = {}
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

    # configure directory
    params = read_yaml(PARAMS_FILE_PATH)
    subdir_path = os.path.join(params.save_plots, "trends")
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)

    for col in numerical_cols:
        X = np.arange(len(df)).reshape(-1, 1)
        y = df[col].values
        model = LinearRegression().fit(X, y)
        slope = model.coef_[0]

        if slope > 0:
            trend = "Upward trend"
        elif slope < 0:
            trend = "Downward trend"
        else:
            trend = "No clear trend"

        trends[col] = trend

        # plotting the trend
        
        plt.figure(figsize=(6, 4))
        sns.regplot(x=X.reshape(-1), y=y, ci=None)
        plt.title(f'Plot: {col} Trend')
        
        plot_file = os.path.join(subdir_path, f'{col}.png')
        plt.savefig(plot_file)
        plt.close()

    return trends