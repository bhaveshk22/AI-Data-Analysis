import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'aiAnalysis'

list_of_files = [
    "data_ingestion/__init__.py",
    "data_ingestion/data_loader.py",
    "data_preprocessing/__init__.py",
    "data_preprocessing/preprocessor.py",
    "data_analysis/__init__.py",
    "artifacts/analysis_plots/storage_for_plots.txt",
    "data_report_generator/__init__.py",
    "data_report_generator/report_generator.py",
    "user_interaction/__init__.py",
    "utils/__init__.py",
    "main.py",
    "params.yaml",
    "requirements.txt",
    "README.md",
    ".gitignore"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'creating empty file: filepath: {filepath}')
    else:
        logging.info(f'{filename} already exists.')
