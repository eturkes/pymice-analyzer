#    This file is part of pymice-analyzer.
#    Copyright (C) 2018  Emir Turkes
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Emir Turkes can be contacted at eturkes@bu.edu

from setuptools import setup

requirements = [
    'certifi',
    'PyMICE'
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock',
    'pytest-qt',
    'pytest-xvfb'
]

setup(
    name='pymice-analyzer',
    version='0.1.0',
    description="A front-end for PyMICE",
    author="Emir Turkes",
    author_email='eturkes@bu.edu',
    url='https://github.com/eturkes/pymice-analyzer',
    packages=['pymice_analyzer', 'pymice_analyzer.images',
              'pymice_analyzer.tests'],
    package_data={'pymice_analyzer.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'PyMICE=pymice_analyzer.application:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='pymice-analyzer',
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
