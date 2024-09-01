import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'aiAnalysis'

list_of_files = [
    "01_data_ingestion/__init__.py",
    "01_data_ingestion/data_loader.py",
    "02_data_preprocessing/__init__.py",
    "02_data_preprocessing/preprocessor.py",
    "03_data_analysis/__init__.py",
    "03_data_analysis/model_pipeline.py",
    "04_report_generation/__init__.py",
    "04_report_generation/report_generator.py",
    "main.py",
    "params.yaml",
    "setup.py",
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
