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

import utils as us


@gy.Gooey(program_name="PyMICE Analyzer")
def parse_args():
    """Use GooeyParser to build up arguments in the script and save the arguments in a
    default json file so that they can be retrieved each time the script is ran.
    """
    stored_args = {}
    # Get the script name without the extension & use it to build up the json filename.
    args_file = "pymice-analyzer-args.json"
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
        help="Input directory containing Intellicage files",
    )
    parser.add_argument(
        "output_directory",
        action="store",
        widget="DirChooser",
        default=stored_args.get("output_directory"),
        help="Output directory to save analysis",
    )
    parser.add_argument(
        "project_name",
        action="store",
        default=stored_args.get("project_name"),
        help="Name of your project",
    )
    parser.add_argument(
        "paradigms",
        action="store",
        default=stored_args.get("paradigms"),
        help="Paradigms to use in the analysis",
    )
    parser.add_argument(
        "start",
        action="store",
        default=stored_args.get("start"),
        help="Start times and dates of the phases",
    )
    parser.add_argument(
        "end",
        action="store",
        default=stored_args.get("end"),
        help="End times and dates of the phases",
    )
    parser.add_argument(
        "excluded_groups",
        action="store",
        default=stored_args.get("excluded_groups"),
        help="Groups to exclude",
    )
    parser.add_argument(
        "excluded_animals",
        action="store",
        default=stored_args.get("excluded_animals"),
        help="Animals to exclude",
    )
    parser.add_argument(
        "comparisons",
        action="store",
        default=stored_args.get("comparisons"),
        help="What comparisons to make",
    )
    parser.add_argument(
        "error",
        action="store",
        default=stored_args.get("error"),
        help="Way error should be measured",
    )
    parser.add_argument(
        "normality",
        action="store",
        default=stored_args.get("normality"),
        help="Which normality tests to use",
    )
    parser.add_argument(
        "variance",
        action="store",
        default=stored_args.get("variance"),
        help="Which variance tests to use",
    )
    parser.add_argument(
        "tests",
        action="store",
        default=stored_args.get("tests"),
        help="Which statistical tests to use",
    )
    parser.add_argument(
        "post_hoc",
        action="store",
        default=stored_args.get("post_hoc"),
        help="Which post hoc tests to use",
    )
    parser.add_argument(
        "plots",
        action="store",
        default=stored_args.get("plots"),
        help="Types of plots to make",
    )
    parser.add_argument(
        "tables",
        action="store",
        default=stored_args.get("tables"),
        help="Types of tables to make",
    )
    args = parser.parse_args()

    # Store the values of the arguments so that it is available on next run.
    with open(args_file, "w") as data_file:
        # Using vars(args) returns the data as a dictionary.
        jn.dump(vars(args), data_file)

    return args


if __name__ == "__main__":
    conf = parse_args()
    us.create_project_layout(
        conf.data_directory, conf.output_directory, conf.project_name
    )
    print("Done")
