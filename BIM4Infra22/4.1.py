# pip install otlmow_template

import logging
from pathlib import Path


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    subset_tool = SubsetTool()
    subset_location = Path('./OTL_AllCasesTestClass.db')
    csv_location = Path('./template_file_text.csv')
