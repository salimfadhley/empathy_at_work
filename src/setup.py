#! /usr/bin/env python
from setuptools import setup
import os

PROJECT_ROOT, _ = os.path.split(__file__)
REVISION = '0.0.1'
PROJECT_NAME = 'empathy_at_work'
PROJECT_AUTHORS = "Salim Fadhley"
PROJECT_EMAILS = 'salimfadhley@gmail.com'
PROJECT_URL = "https://github.com/salimfadhley/eztable"
SHORT_DESCRIPTION = 'Simple in-memory tables in pure Python.'

try:
    DESCRIPTION = open(os.path.join(PROJECT_ROOT, "readme.rst")).read()
except IOError:
    DESCRIPTION = SHORT_DESCRIPTION

setup(
    name=PROJECT_NAME.lower(),
    version=REVISION,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    packages=['empathy_at_work',],
    zip_safe=True,
    include_package_data=False,
    install_requires=['eztable'],
    test_suite='nose.collector',
    tests_require=['mock', 'nose', 'coverage'],
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    license='MIT'
)
