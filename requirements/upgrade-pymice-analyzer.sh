#!/bin/sh

#    This file is part of pymice-analyzer.
#    Copyright (C) 2018-2019  Emir Turkes
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

# This script keeps the pymice-analyzer conda env up-to-date. It first upgrades all
# conda packages and then all pip packages. To help ensure the most important packages
# stay at the highest version possible, we upgrade them manually after upgrading all of
# the packages. pip is also upgraded manually because conda keeps it at an unusually
# old version.

# Call the script using ". ./upgrade-pymice-analyzer.sh". Note the first dot, this is
# necessary to make conda available by executing the script in the current shell.

echo Upgrade\ pymice-analyzer\ conda\ environment: \
    && conda activate pymice-analyzer \
    && conda update --all \
    && conda list | grep "<pip>" | cut -d " " -f 1 | xargs pip install -U \
    && conda update anaconda wxpython gitpython \
    && pip install -U gooey pymice pip
