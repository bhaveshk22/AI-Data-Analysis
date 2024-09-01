import pandas as pd

def load_data(filepath):
    # Load CSV, Excel, or JSON data
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        return pd.read_excel(filepath)
    elif filepath.endswith('.json'):
        return pd.read_json(filepath)
    else:
        raise ValueError("Unsupported file format.")
