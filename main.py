from utils import *
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
from user_interaction import process_query


#Loading the dataset
logger.info('Data Loading Started')
params = read_yaml(PARAMS_FILE_PATH)
data = load_data(params.data_path)
logger.info("Data Loaded Successfully")


#Analysing and Preprocessing dataset
logger.info("Data Analysis and Preprocessing Started")
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

import json

# with open('data.json', 'w') as json_file:
#     json.dump(summary, json_file, indent=4)

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


#handling queries related to data analysis
while True:
    query = input('\nAsk about data analysis (type exit to stop): ').strip()
    
    # Check if the user wants to exit
    if query.lower() == 'exit':
        print("Exiting the program. Thank you!")
        break
    
    # Check if the input is empty
    elif not query:
        print("You didn't enter any query. Please try again.")
        continue
    
    # Process the query and get the response
    else:
        response = process_query(query, data, summary)
        print(f"Response: {response}")