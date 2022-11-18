# pip install otlmow_template

import logging
from pathlib import Path

from otlmow_template.SubsetTemplateCreator import SubsetTemplateCreator

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    template_creator = SubsetTemplateCreator()
    subset_location = Path('./camera_steun.db')
    csv_location = Path('./template_file.csv')

    template_creator.generate_template_from_subset(path_to_subset=subset_location,
                                                   path_to_template_file_and_extension=csv_location,
                                                   split_per_type=True)
