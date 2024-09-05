import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
import os
from utils import *

def pca_feature_importance(data: pd.DataFrame, n_components=0.95):
    """
    Uses PCA to determine the contribution of each feature to the principal components and plots the feature importance.

    Parameters:
    - data: pd.DataFrame - The input DataFrame.
    - n_components: float - Percentage of variance to cover.

    Returns:
    - pca_df: pd.DataFrame - DataFrame containing feature contributions to each component.
    """
    # Label or One hot encoding categorical features
    categorical_cols = [col for col in data.columns if data[col].dtype == 'object']

    cat_cols_label = [col for col in categorical_cols if data[col].nunique() > 5]
    cat_cols_ohe = [col for col in categorical_cols if data[col].nunique() <= 5]

    for col in cat_cols_label:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])

    data = pd.get_dummies(data, columns=cat_cols_ohe, dtype=int)


    # Standardize the data
    data_std = (data - data.mean()) / data.std()

    # Apply PCA
    pca = PCA(n_components=n_components)
    pca.fit(data_std)

    # Get the loading scores (contribution of each feature to the principal components)
    loadings = pd.DataFrame(pca.components_.T, columns=[f'PC{i+1}' for i in range(pca.n_components_)], index=data.columns)

    # Plotting the feature importance
    plt.figure(figsize=(10, 8))
    loadings.plot(kind='bar', figsize=(12, 8))
    plt.title('Feature Importance Based on PCA Loadings')
    plt.ylabel('Contribution to Principal Components')
    plt.xlabel('Features')

    # Save the plot
    params = read_yaml(PARAMS_FILE_PATH)
    plot_file = os.path.join(params.save_plots, "pca_analysis.png")
    plt.savefig(plot_file)
    plt.close()

    return loadings.to_dict()


