import pandas as pd
import os
import seaborn as sns
from utils import *
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder


def feature_importance(df, target_column, top_n=10):
    """
    Uses Random Forest to determine feature importance, plot the top important features,
    and save the plot with importance labeled in percentage.

    Parameters:
    - df: pandas dataframe
    - target_column: column that is the target of the analysis
    - top_n: int - The number of top important features to plot.
    """
    
    # Label or One hot encoding categorical features
    categorical_cols = [col for col in df.columns if df[col].dtype == 'object']

    cat_cols_label = [col for col in categorical_cols if df[col].nunique() > 5]
    cat_cols_ohe = [col for col in categorical_cols if df[col].nunique() <= 5]

    for col in cat_cols_label:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    df = pd.get_dummies(df, columns=cat_cols_ohe, dtype=int)

    # separating features and target column
    features = df.drop(columns=[target_column])
    target = df[target_column]

    # Fit the model
    model = RandomForestRegressor(random_state=0)
    model.fit(features, target)

    # Get feature importances
    importance = model.feature_importances_

    # Create a DataFrame for feature importance
    feature_importance_df = {
        'Feature': features.columns,
        'Importance': importance
    }

    # Sort features by importance
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

    # Plot the top_n important features
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Importance', y='Feature', data=feature_importance_df.head(top_n), palette='viridis')
    plt.title(f'Top {top_n} Important Features')
    plt.xlabel('Importance (%)')
    plt.ylabel('Feature')

    # Convert importance to percentage and label them
    for index, value in enumerate(feature_importance_df['Importance'].head(top_n)):
        plt.text(value, index, f'{value * 100:.2f}%', va='center')

    # Save the plot
    params = read_yaml(PARAMS_FILE_PATH)
    plot_file = os.path.join(params.save_plots, 'feature_importance_plot.png')
    plt.savefig(plot_file)
    plt.close()

    return feature_importance_df


