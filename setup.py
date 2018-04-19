#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

if __name__ == "__main__":

    with open('README.rst', 'r') as f:
        long_description = f.read()

    setup(
        long_description=long_description,
        package_dir={'': str('src')}
    )