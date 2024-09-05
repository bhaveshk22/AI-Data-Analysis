
# **DataInsight Engine**

DataInsight Engine is a comprehensive tool designed to streamline the data analysis process. It automates key steps such as loading datasets, preprocessing data, analyzing it using various statistical and machine learning techniques, generating insightful reports, and answering user queries about the data. This engine is perfect for quick, automated insights into any dataset.

## **Features**
- Load datasets from CSV, JSON, or Excel formats.
- Perform data preprocessing to handle missing values, scaling, and more.
- Analyze data trends, patterns, and key insights using multiple ML algorithms.
- Generate detailed analysis reports.
- Handle natural language queries about the dataset, providing specific answers.

## **Project Structure**
- **data_ingestion/**: Handles loading datasets from various file formats.
- **data_preprocessing/**: Preprocesses the data (e.g., missing value imputation, normalization).
- **data_analysis/**: Performs data analysis using algorithms like regression, random forest, and PCA.
- **data_report_generator/**: Generates a report based on the analysis.
- **user_interaction/**: Handles the user queries and generates response in command line interface.
- **logger/**: Custom logger module
- **research/**: Notebook for various experiments.
- **utils/**: Common utility tools for various purposes.
- **main.py**: The entry point to run the engine, guiding users through each step interactively.
- **params.yaml**: Configuration file for parameters like file paths, preprocessing options, etc.

## **Installation**
1. To get started with the DataInsight Engine, move to the source code:


```bash
cd Source_Code
```

2. Set the path of the dataset in params.yaml

3. Create a virtual environment

```bash
python -m venv env

env\Scripts\activate

# if using git bash
source env/Scripts/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## **Usage**
Run the engine with the following command:

```bash
python template.py
python main.py
```

The engine will guide you through the following steps:
1. Loading your dataset.
2. Preprocessing it.
3. Performing data analysis.
4. Generating a report.
5. Answering queries related to the dataset.

## **Query Handling**
DataInsight Engine allows you to ask questions like:
- "What is the number of outliers in 'column name'?"
- "Give me the summary of the data?"
- "What is the percentage of the missing values in 'column name'?"

The engine uses a basic NLP model to interpret and respond to these questions.

