from pathlib import Path
from utils import read_yaml
from logger import logger
from data_ingestion import load_data
from data_preprocessing import preprocess_data
from data_analysis import (analyze_dataset,
                           summarize_correlations,
                           bivariate_plot,
                           regression_trend,
                           feature_importance,
                           pca_feature_importance)
from data_report_generator import generate_report


#Loading the dataset
logger.info('Data Loading Started')
params = read_yaml(Path("params.yaml"))
data = load_data(params.data_path)
logger.info("Data Loaded Successfully")


#Analysing and Preprocessing dataset
logger.info("Data Analysis and Prerprocessing Started")
statistics, description = analyze_dataset(data)

data = preprocess_data(data)

correlations = summarize_correlations(data)
bivariate_plot(data)
trends = regression_trend(data)
pca_summary = pca_feature_importance(data)

summary = {
    'Statistics' : statistics,
    'Description': description,
    'Trends': trends,
    'Correlations': correlations,
    'PCA Summary': pca_summary
}

target = input("Enter the target variable for feature importance (type 'None' if there is no target): ")
if target.lower() != "none":
    feature_imp = feature_importance(data, target)
    summary['Feature Importance'] = feature_imp

logger.info("Data Analyzed and Preprocessed Successfully")

# print(summary)

# generating report
logger.info("Generating Report...")

html = generate_report(summary,data)
with open("report.html", 'w') as f:
    f.write(html)

logger.info('Reported Generated Successfully')