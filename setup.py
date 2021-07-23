#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='gitflow_authors_linter',
    version='0.0.1',
    description='Provides additional functionality to gitflow-linter tool',
    long_description=read("README.md"),
    author='Poul Fighter',
    author_email='fighter.poul@gmail.com',
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    python_requires='>3.8',
    license=read("LICENSE"),
    install_requires=[
        'PyYAML>=5.4.1',
        'GitPython>=3.1.17',
        'click>=7',
        'gitflow_linter>=0.0.4'
    ]
)