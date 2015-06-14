#!/usr/bin/env python

from setuptools import setup

description = 'Create json logging output for python' + \
              'nosetests unittest framework',

setup(
    name='nosetests-json-extended',
    version='0.1.0',
    author='Thijs Schenkelaars',
    author_email='thijs@schenkelaars.nl',
    description=description,
    url='http://github.com/thschenk/nosetests-json-extended',
    packages=['nosetests_json_extended'],
    zip_safe=False,
    entry_points={
        'nose.plugins.0.10': [
            'nosetests_json_extended = ' +
            'nosetests_json_extended.plugin:JsonExtendedPlugin'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing'
    ],
    long_description=open('README.rst', 'r').read()
)
