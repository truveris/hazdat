"""Setup for HazDat."""
from codecs import open
from os import path
from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hazdat',
    version='0.1.0',
    description='HazDat Hazardous Data Library',
    long_description=long_description,
    url='https://github.com/truveris/hazdat',
    author='Truveris Inc.',
    author_email='dev@truveris.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['hazdat'],
    install_requires=['wrapt'],
    extras_require={
        'dev': ['tox'],
        'cover': ['coverage'],
    },
)
