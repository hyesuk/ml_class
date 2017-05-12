# -*- coding: utf-8 -*-
"""Setup for ml-class."""
from setuptools import setup, find_packages

requires = [
        'simplejson',
        'mrjob',
        'testify',
        'unittest2',
        ]

setup(
        name='ml-class',
        description='Practice for machine learning algorithms.',
        author='Hyesuk Byun',
        url='https://github.com/hyesuk/ml_class',
        packages=find_packages(),
        install_requires=requires,
        tests_require=requires,
        )
