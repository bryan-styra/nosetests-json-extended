#!/usr/bin/env python

from setuptools import setup

description = 'Create extended json logging output for python' + \
              'nosetests unittest framework',

setup(
    name='nosetests-json-extended',
    version='0.0.0',
    author='Thijs Schenkelaars',
    author_email='thijs@schenkelaars.nl',
    description=description,
    url='http://github.com/thschenk/nosetests-json-extended',
    packages=['nosetests_json_extended'],
    zip_safe=False,
    entry_points={
        'nose.plugins.0.10': [
            'nosetests_json_extended = nosetests_json_extended.plugin:JsonExtendedPlugin'
        ]
    }
)
