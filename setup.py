from setuptools import setup, find_packages

setup(
    name = 'sfmc-cli',
    version = '1.0.0',
    packages =find_packages(),
    entry_points = {
        'console_scripts': [
            'sfmc-cli = src.main:sfmc_cli'
        ]
    })
