import os
from utils import *
import urllib.parse

def generate_report(summary,data):
    
    # configuring path for loading plots
    params = read_yaml(PARAMS_FILE_PATH)

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Report</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            h1 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1 class="center">Analysis Report</h1>
    """
    
    
    overall = summary['Statistics']['overall']
    html += f"""
    <div class="box">
    <h2>Overall Summary:</h2>
    <table>
    <tr>
        <th>Shape</th>
        <td>: {overall['shape']}</td>
    </tr>
    <tr>
        <th>Missing</th>
        <td>: {overall['missing_values']}</td>
    </tr>
    <tr>
        <th>Missing (%)</th>
        <td>: {overall['missing_values_percentage']}</td>
    </tr>
    <tr>
        <th>Duplicate Rows</th>
        <td>: {overall['duplicate_rows']}</td>
    </tr>
    <tr>
        <th>Duplicate Rows (%)</th>
        <td>: {overall['duplicate_rows_percentage']}</td>
    </tr>
    </table>
    </div>
    """

    for cols in data.columns:
        column = summary['Statistics'][cols]
        html += f"""
        <div class="box">
        <h2>{cols}:</h2>
        <table>
        <tr>
            <th>Missing</th>
            <td>: {column['missing_values']}</td>
        </tr>
        <tr>
            <th>Missing (%)</th>
            <td>: {column['missing_values_percentage']}</td>
        </tr>
        <tr>
            <th>Distinct</th>
            <td>: {column['distinct_values']}</td>
        </tr>
        <tr>
            <th>Distinct (%)</th>
            <td>: {column['distinct_values_percentage']}</td>
        </tr>
        
        """
        
        if os.path.exists(os.path.join(params.distribution, f'{cols}.png')):
            desc = summary['Description'][cols]
            html += f"""
            <tr>
                <th>Outliers (%)</th>
                <td>: {column['outliers']}</td>
            </tr>
            <tr>
                <th>Outliers (%)</th>
                <td>: {column['outliers_percentage']}</td>
            </tr>
            <tr>
                <th>Count</th>
                <td>: {desc['count']}</td>
            </tr>
            <tr>
                <th>Mean</th>
                <td>: {round(desc['mean'],2)}</td>
            </tr>
            <tr>
                <th>Standard Deviation</th>
                <td>: {round(desc['std'],2)}</td>
            </tr>
            <tr>
                <th>Minimum</th>
                <td>: {desc['min']}</td>
            </tr>
            <tr>
                <th>Q1</th>
                <td>: {round(desc['25%'],2)}</td>
            </tr>
            <tr>
                <th>Q2</th>
                <td>: {round(desc['50%'],2)}</td>
            </tr>
            <tr>
                <th>Q3</th>
                <td>: {round(desc['75%'],2)}</td>
            </tr>
            <tr>
                <th>Maximum</th>
                <td>: {desc['max']}</td>
            </tr>
            </table>
            <img src={os.path.join(params.distribution, urllib.parse.quote(f'{cols}.png'))} alt={urllib.parse.quote(cols)}.png>
            </div>
            """
            
        else:
            html += """
            </table>
            </div>
            """

    for file in os.listdir(params.trends):
        filename = str(file).removesuffix('.png')
        filepath = os.path.join(params.trends, urllib.parse.quote(file))
        html += f"""
        <div class="plot">
            <h2>Trend: {filename}</h2>
            <h3>{summary['Trends'][filename]}</h3>
            <img src={filepath} alt={urllib.parse.quote(filename)}>
        </div>
        """

    html += f"""
    <div class="plot">
        <h2>Correlation</h2>
       <img src={urllib.parse.quote(params.correlation)} alt="correlation">
    </div>
    <div>
        <h2>PCA Summary</h2>
        <p>PCA calculates feature importance by assessing the contribution of each individual feature to the newly transformed features.</p>
        <img src={urllib.parse.quote(params.pca_summary)} alt="pca">
    </div>
    """
    
    if os.path.exists(params.feature_imp):
        html += f"""
        <div class="plot">
            <h2>Feature Importance Using Randomforest</h2>
            <img src={urllib.parse.quote(params.feature_imp)} alt="correlation">
        </div>
        """
    
    for file in os.listdir(params.bivariate):
        filename = str(file).removesuffix('.png')
        filepath = os.path.join(params.bivariate, urllib.parse.quote(file))
        html += f"""
        <div class="plot">
            <h2>{filename}</h2>
            <img src={filepath} alt={urllib.parse.quote(filename)}>
        </div>
        """
    
    html += """
    
    """
    
    
    
    html += """
    </body>
    </html>
    """
    
    return html