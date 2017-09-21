"""
A setuptools based setup module.
"""

from setuptools import setup

setup(
    name='dita_link_validator',
    version='1.0',
    description='CLI tool that checks html links in a ditamap',
    author='Miklos Duma',
    author_email='duma.miklos@gmail.com',
    url='http://github.com/miklosduma/dita_link_validator',
    packages=['dita_link_validator'],
    license='MIT',
    install_requires=['requests', 'termcolor'],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)
