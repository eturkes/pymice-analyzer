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
    # parser.add_argument(
    #     "--verbose",
    #     help="be verbose",
    #     dest="verbose",
    #     action="store_true",
    #     default=False,
    # )
    subs = parser.add_subparsers()

    universal_parser = subs.add_parser(
        "universal_settings",
        prog="Universal Settings",
        help="Blanket settings for all paradigms",
    )
    num_visits_parser = subs.add_parser("num_visits", prog="Number of Visits")
    num_pokes_parser = subs.add_parser("num_pokes", prog="Number of Nosepokes")
    visit_dur_parser = subs.add_parser("visit_dur", prog="Visit Duration")
    poke_dur_parser = subs.add_parser("poke_dur", prog="Nosepoke Duration")
    time_corners_parser = subs.add_parser("time_corners", prog="Time to All Corners")
    time_pokes_parser = subs.add_parser("time_pokes", prog="Time to All Nosepokes")
    corner_pref_parser = subs.add_parser("corner_pref", prog="Corner Preference")
    door_pref_parser = subs.add_parser("door_pref", prog="Door Preference")
    zig_zag_parser = subs.add_parser("zig_zag", prog="Zig-zag Visits")
    perimeter_parser = subs.add_parser("perimeter", prog="Perimeter Visits")
    overtake_parser = subs.add_parser("overtake", prog="Overtake Occurrences")

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
        "out_dir",
        metavar="Output Directory",
        widget="DirChooser",
        default=stored_args.get("out_dir"),
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

    paradigm_list = [
        num_visits_parser,
        num_pokes_parser,
        visit_dur_parser,
        poke_dur_parser,
        time_corners_parser,
        time_pokes_parser,
        corner_pref_parser,
        door_pref_parser,
        zig_zag_parser,
        perimeter_parser,
        overtake_parser,
    ]
    for paradigm_parser in paradigm_list:
        paradigm_parser.add_argument(
            "data_dir",
            metavar="Data Directory",
            widget="DirChooser",
            default=stored_args.get("data_dir"),
            help="Input directory containing Intellicage files",
        )
        paradigm_parser.add_argument(
            "out_dir",
            metavar="Output Directory",
            widget="DirChooser",
            default=stored_args.get("out_dir"),
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
    return args


if __name__ == "__main__":
    conf = parse_args()
    us.create_project_layout(conf.data_dir, conf.out_dir, conf.proj_name)
    print("Done")
