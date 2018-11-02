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


@gy.Gooey(program_name="PyMICE Analyzer", show_sidebar=True, sidebar_title="Paradigms")
def parse_args():
    """Use GooeyParser to build up arguments in the script and save the arguments in a
    default json file so that they can be retrieved each time the script is ran.
    """
    stored_args = {}
    args_file = "pymice-analyzer-args.json"
    # Read in the prior arguments as a dictionary.
    if os.path.isfile(args_file):
        with open(args_file) as data_file:
            stored_args = jn.load(data_file)
    parser = gy.GooeyParser(description="GPLv3 - Emir Turkes; Phenovance LLC")
    subs = parser.add_subparsers()

    universal_parser = subs.add_parser(
        "universal_settings",
        prog="Universal Settings",
        help="Blanket settings for all paradigms",
    )
    universal_parser.add_argument(
        "proj_name",
        metavar="Project Name",
        default=stored_args.get("proj_name"),
        help="Name of your project",
    )
    universal_parser.add_argument(
        "run_all",
        metavar="Run pipeline after generating scripts?",
        widget="Dropdown",
        choices=["Yes", "No"],
        default=stored_args.get("run_all"),
        help="If unchecked use run-all.py in project directory",
    )
    universal_parser.add_argument(
        "data_dir",
        metavar="Data Directory",
        widget="DirChooser",
        default=stored_args.get("data_dir"),
        help="Input directory containing Intellicage files",
    )
    universal_parser.add_argument(
        "proj_dir",
        metavar="Output Directory",
        widget="DirChooser",
        default=stored_args.get("proj_dir"),
        help="Output directory to save analysis",
    )
    universal_parser.add_argument(
        "start",
        metavar="Start",
        widget="DateChooser",
        default=stored_args.get("start"),
        help="Start times and dates of the phases",
    )
    universal_parser.add_argument(
        "end",
        metavar="End",
        widget="DateChooser",
        default=stored_args.get("end"),
        help="End times and dates of the phases",
    )
    universal_parser.add_argument(
        "plots",
        metavar="Plots",
        widget="Dropdown",
        choices=["Bar", "Line", "Box"],
        default=stored_args.get("plots"),
        help="Types of plots to make",
    )
    universal_parser.add_argument(
        "tables",
        metavar="Tables",
        widget="Dropdown",
        choices=["Normality", "Variance", "Post-hoc"],
        default=stored_args.get("tables"),
        help="Types of tables to make",
    )
    universal_parser.add_argument(
        "comparisons",
        metavar="Comparisons",
        widget="Dropdown",
        choices=["Between Group", "Within Group"],
        default=stored_args.get("comparisons"),
        help="What comparisons to make",
    )
    universal_parser.add_argument(
        "error",
        metavar="Error",
        widget="Dropdown",
        choices=["SEM", "SD"],
        default=stored_args.get("error"),
        help="Way error should be measured",
    )
    universal_parser.add_argument(
        "normality",
        metavar="Normality",
        widget="Dropdown",
        choices=["Shapiro-Wilk", "Kolmogorov-Smirnov"],
        default=stored_args.get("normality"),
        help="Which normality tests to use",
    )
    universal_parser.add_argument(
        "variance",
        metavar="Variance",
        widget="Dropdown",
        choices=["Levene", "Brown-Forsythe"],
        default=stored_args.get("variance"),
        help="Which variance tests to use",
    )
    universal_parser.add_argument(
        "tests",
        metavar="Tests",
        widget="Dropdown",
        choices=["Kruskal-Wallis", "Mann-Whitney"],
        default=stored_args.get("tests"),
        help="Which statistical tests to use",
    )
    universal_parser.add_argument(
        "post_hoc",
        metavar="Post-hoc",
        widget="Dropdown",
        choices=["Dunn", "Tukey"],
        default=stored_args.get("post_hoc"),
        help="Which post hoc tests to use",
    )
    universal_parser.add_argument(
        "--excluded_groups",
        metavar="Excluded Groups",
        default=stored_args.get("excluded_groups"),
        help="Groups to exclude",
    )
    universal_parser.add_argument(
        "--excluded_animals",
        metavar="Excluded Animals",
        default=stored_args.get("excluded_animals"),
        help="Animals to exclude",
    )

    all_paradigms = {
        "num_visits": "Number of Visits",
        "num_pokes": "Number of Nosepokes",
        "visit_dur": "Visit Duration",
        "poke_dur": "Nosepoke Duration",
        "time_corners": "Time to All Corners",
        "time_pokes": "Time to All Pokes",
        "corner_pref": "Corner Preferences",
        "door_pref": "Door Preference",
        "zig_zag": "Zig-zag Visits",
        "perimeter": "Perimeter Visits",
        "overtake": "Overtake Occurrences",
    }
    for paradigm in all_paradigms:
        paradigm_parser = subs.add_parser(paradigm, prog=all_paradigms[paradigm])
        paradigm_parser.add_argument(
            "data_dir",
            metavar="Data Directory",
            widget="DirChooser",
            default=stored_args.get("data_dir"),
            help="Input directory containing Intellicage files",
        )
        paradigm_parser.add_argument(
            "proj_dir",
            metavar="Output Directory",
            widget="DirChooser",
            default=stored_args.get("proj_dir"),
            help="Output directory to save analysis",
        )
        paradigm_parser.add_argument(
            "start",
            metavar="Start",
            widget="DateChooser",
            default=stored_args.get("start"),
            help="Start times and dates of the phases",
        )
        paradigm_parser.add_argument(
            "end",
            metavar="End",
            widget="DateChooser",
            default=stored_args.get("end"),
            help="End times and dates of the phases",
        )
        paradigm_parser.add_argument(
            "plots",
            metavar="Plots",
            widget="Dropdown",
            choices=["Bar", "Line", "Box"],
            default=stored_args.get("plots"),
            help="Types of plots to make",
        )
        paradigm_parser.add_argument(
            "tables",
            metavar="Tables",
            widget="Dropdown",
            choices=["Normality", "Variance", "Post-hoc"],
            default=stored_args.get("tables"),
            help="Types of tables to make",
        )
        paradigm_parser.add_argument(
            "comparisons",
            metavar="Comparisons",
            widget="Dropdown",
            choices=["Between Group", "Within Group"],
            default=stored_args.get("comparisons"),
            help="What comparisons to make",
        )
        paradigm_parser.add_argument(
            "error",
            metavar="Error",
            widget="Dropdown",
            choices=["SEM", "SD"],
            default=stored_args.get("error"),
            help="Way error should be measured",
        )
        paradigm_parser.add_argument(
            "normality",
            metavar="Normality",
            widget="Dropdown",
            choices=["Shapiro-Wilk", "Kolmogorov-Smirnov"],
            default=stored_args.get("normality"),
            help="Which normality tests to use",
        )
        paradigm_parser.add_argument(
            "variance",
            metavar="Variance",
            widget="Dropdown",
            choices=["Levene", "Brown-Forsythe"],
            default=stored_args.get("variance"),
            help="Which variance tests to use",
        )
        paradigm_parser.add_argument(
            "tests",
            metavar="Tests",
            widget="Dropdown",
            choices=["Kruskal-Wallis", "Mann-Whitney"],
            default=stored_args.get("tests"),
            help="Which statistical tests to use",
        )
        paradigm_parser.add_argument(
            "post_hoc",
            metavar="Post-hoc",
            widget="Dropdown",
            choices=["Dunn", "Tukey"],
            default=stored_args.get("post_hoc"),
            help="Which post hoc tests to use",
        )
        paradigm_parser.add_argument(
            "--excluded_groups",
            metavar="Excluded Groups",
            default=stored_args.get("excluded_groups"),
            help="Groups to exclude",
        )
        paradigm_parser.add_argument(
            "--excluded_animals",
            metavar="Excluded Animals",
            default=stored_args.get("excluded_animals"),
            help="Animals to exclude",
        )

    args = parser.parse_args()
    # Store the values of the arguments so that it is available on next run.
    with open(args_file, "w") as data_file:
        # Using vars(args) returns the data as a dictionary.
        jn.dump(vars(args), data_file)
    return args, all_paradigms


if __name__ == "__main__":
    conf = parse_args()
    args = conf[0]
    all_paradigms = conf[1]
    proj_path = os.path.join(args.proj_dir, args.proj_name.lower().replace(" ", "_"))
    us.create_project_layout(args.data_dir, proj_path)
    us.create_notebook(
        all_paradigms,
        args.data_dir,
        proj_path,
        args.proj_name,
        args.start,
        args.end,
        args.excluded_groups,
        args.excluded_animals,
        args.comparisons,
        args.error,
        args.normality,
        args.variance,
        args.tests,
        args.post_hoc,
        args.plots,
        args.tables,
    )
    print("Done")
