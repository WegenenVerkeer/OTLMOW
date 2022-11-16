# pip install otlmow_modelbuilder

import logging
from pathlib import Path

from otlmow_converter.OtlmowConverter import OtlmowConverter
from otlmow_model.Helpers.GenericHelper import print_overview_assets

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    converter = OtlmowConverter()

    cameras = converter.create_assets_from_file(filepath=Path('./cameras_open_data.csv'))
    print_overview_assets(cameras)

    ptz = list(filter(lambda c: c.isActief and c.isPtz, cameras))

    converter.create_file_from_assets(filepath=Path('./ptz_open_data.json'),
                                      list_of_objects=ptz)
