#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='swancontents',
      version='0.0.8',
      description='Jupyter Notebook filesystem with Projects',
      include_package_data=True,
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'notebook==6.0.*',
          'tornado',
          'jupyter_core'
      ],
  )
