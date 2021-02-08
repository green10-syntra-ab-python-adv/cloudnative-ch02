# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='super simple flask demo',
    long_description=readme,
    author='Hans Vandenbogaerde',
    author_email='hans.vandenbogaerde@gmail.com',
    url='NA',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

