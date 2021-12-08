#! python
# -*- coding: utf-8 -*-

import argparse
import runpy
import os

current = os.path.realpath(os.path.dirname(__file__))

__version__ = runpy.run_path(
    os.path.join(current, "version.py"))["__version__"]


def get_args(args_list: list):
    parser = argparse.ArgumentParser(
        description="data preparation tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Commons options

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s {}'.format(__version__))

    parser.add_argument(
        "--imagedir",
        help="Directory containing the images",
        dest="IMAGES_DIR",
        required=True)

    parser.add_argument(
        "--xmldir",
        help="Directory containing the xml files",
        dest="XML_DIR",
        required=True)

    parser.add_argument(
        "--outputdir",
        help="Directory to output the files to",
        dest="OUTPUT_DIR",
        required=True)

    args = parser.parse_args(args_list)

    return args
