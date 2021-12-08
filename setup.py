#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import runpy
from setuptools import setup, find_packages


current = os.path.realpath(os.path.dirname(__file__))

__version__ = runpy.run_path(
    os.path.join(current, "dataprep", "version.py"))["__version__"]

with open(os.path.join(current, 'requirements.txt')) as f:
    requires = f.read().splitlines()

setup(
    name="dataprep",
    description="Tools to pre-process images with their xmls",
    license="",
    url="",
    version=__version__,
    author="Andrea Vitali",
    author_email="andrea.vitali@cedacri.it",
    maintainer="Andrea Vitali",
    maintainer_email="andrea.vitali@cedacri.it",
    packages=find_packages(exclude=('test','venv')),
    platforms=["Linux","Windows"],
    keywords=["coco", "xml", "dataset", "ecc"],
    install_requires=requires,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Indipendent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    entry_points={'console_scripts': [
        "dataprep = dataprep.__main__:main",
    ]},
)
