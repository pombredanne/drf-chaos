#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='drf_chaos',
    version='0.1',
    description='DRF Extension to test API failures',
    long_description=open('README.rst').read(),
    author='Alessio Di Stasio',
    author_email='aledista@gmail.com',
    url='https://github.com/aledista/drf-chaos',
    license='BSD',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'djangorestframework>=2.3.5'
        'wrapt>=1.10'
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    test_suite='runtests.runtests',
    extras_require={
        'tests': [
            'Django>=1.6',
            'flake8',
            'mock',
            'pytest',
        ],
    },
)