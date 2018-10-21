#!/usr/bin/env python3
# -*- coding: utf-8 -*

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

"""The main CLI and GUI routine."""

import os
import json as jn

import gooey as gy


@gy.Gooey(program_name="PyMICE Analyzer")
def parse_args():
    """Use GooeyParser to build up arguments in the script and save the arguments in a
    default json file so that they can be retrived each time the script is ran.
    """

    stored_args = {}
    # Get the script name without the extension & use it to build up the json filename.
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    args_file = "{}-args.jn".format(script_name)
    # Read in the prior arguments as a dictionary.
    if os.path.isfile(args_file):
        with open(args_file) as data_file:
            stored_args = jn.load(data_file)
    parser = gy.GooeyParser(description="PyMICE Analyzer")
    parser.add_argument(
        "data_directory",
        action="store",
        default=stored_args.get("data_directory"),
        widget="DirChooser",
        help="Source directory containing Intellicage files",
    )
    parser.add_argument(
        "output_directory",
        action="store",
        widget="DirChooser",
        default=stored_args.get("output_directory"),
        help="Output directory to save analysis",
    )
    args = parser.parse_args()
    # Store the values of the arguments so that it is available on next run.
    with open(args_file, "w") as data_file:
        # Using vars(args) returns the data as a dictionary
        jn.dump(vars(args), data_file)
    return args


if __name__ == "__main__":
    CONF = parse_args()
    print("Done")
