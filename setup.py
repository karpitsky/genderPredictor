#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.1.0'

setup(
    name='gendorpredictor',
    version=VERSION,
    description='GenderPredictor is a wrapper around NLTK\'s Naive Bayes classifier for predicting the gender given a name.',
    author='Stephen Holiday',
    author_email='stephen.holiday@gmail.com',
    license='BSD',
    url='https://github.com/sholiday/genderPredictor',
    keywords=['Gender', 'Python'],
    packages=['genderpredictor'],
    install_requires=[
        'nltk',
    ],
)