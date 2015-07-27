#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import paginator

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = paginator.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='dj-paginator',
    version=version,
    description="""A super-simple set of pagination tools for Django 1.8+""",
    long_description=readme + '\n\n' + history,
    author='Daniel Roy Greenfeld',
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/dj-paginator',
    packages=[
        'paginator',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='dj-paginator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
