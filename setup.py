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


import setuptools as st


st.setup(
    name="PyMICE-analyzer",
    version="0.1.0",
    description="A PyMICE project creator and pipeline manipulator",
    author="Emir Turkes",
    author_email="eturkes@bu.edu",
    url="https://github.com/eturkes/pymice-analyzer",
    packages=["pymice_analyzer"],
    entry_points={"console_scripts": ["PyMICE-analyzer=pymice_analyzer.main:main"]},
    zip_safe=False,
    keywords="PyMICE-analyzer",
    classifiers=["Programming Language :: Python :: 3.6"],
)
