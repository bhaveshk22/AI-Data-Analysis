import numpy as np
from sklearn.linear_model import LinearRegression


def regression_trend(df):
    """
    Uses Linear Regression to identify trends in the data.
    """
    trends = {}
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

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

    return trends