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
    parser = gy.GooeyParser(
        description="GPLv3 - Emir Turkes; Phenovance LLC"
    )
    subs = parser.add_subparsers()

    universal_parser = subs.add_parser("Universal Settings")
    num_visits_parser = subs.add_parser("Number of Visits")
    num_pokes_parser = subs.add_parser("Number of Nosepokes")
    visit_dur_parser = subs.add_parser("Visit Duration")
    poke_dur_parser = subs.add_parser("Nosepoke Duration")
    time_corners_parser = subs.add_parser("Time to All Corners")
    time_pokes_parser = subs.add_parser("Time to All Nosepokes")
    corner_pref_parser = subs.add_parser("Corner Preference")
    door_pref_parser = subs.add_parser("Door Preference")
    zig_zag_parser = subs.add_parser("Zig-zag Visits")
    perimeter_parser = subs.add_parser("Perimeter Visits")
    overtake_parser = subs.add_parser("Overtake Occurrences")

    universal_parser.add_argument(
        "Project Name", action="store", help="Name of your project"
    )
    universal_parser.add_argument(
        "Run pipeline after generating scripts?",
        action="store",
        widget="CheckBox",
        help="   If unchecked, use 'run-all.py' in project directory.",
    )
    universal_parser.add_argument(
        "Data Directory",
        action="store",
        widget="DirChooser",
        help="Input directory containing Intellicage files",
    )
    universal_parser.add_argument(
        "Output Directory",
        action="store",
        widget="DirChooser",
        help="Output directory to save analysis",
    )
    universal_parser.add_argument(
        "Start",
        action="store",
        widget="DateChooser",
        help="Start times and dates of the phases",
    )
    universal_parser.add_argument(
        "End",
        action="store",
        widget="DateChooser",
        help="End times and dates of the phases",
    )
    universal_parser.add_argument(
        "Plots",
        action="store",
        widget="Listbox",
        nargs="*",
        choices=["Bar", "Line", "Box"],
        default=["Bar"],
        help="Types of plots to make",
    )
    universal_parser.add_argument(
        "Tables",
        action="store",
        widget="Listbox",
        nargs="*",
        choices=["Normality", "Variance", "Post-hoc"],
        default=["Variance", "Post-hoc"],
        help="Types of tables to make",
    )
    universal_parser.add_argument(
        "Comparisons",
        action="store",
        widget="Dropdown",
        nargs="*",
        choices=["Between Group", "Within Group"],
        default="Between Group",
        help="What comparisons to make",
    )
    universal_parser.add_argument(
        "Error",
        action="store",
        widget="Dropdown",
        nargs="*",
        choices=["SEM", "SD"],
        default="SEM",
        help="Way error should be measured",
    )
    universal_parser.add_argument(
        "Normality",
        action="store",
        widget="Dropdown",
        nargs="*",
        choices=["Shapiro–Wilk", "Kolmogorov–Smirnov"],
        default="Shapiro–Wilk",
        help="Which normality tests to use",
    )
    universal_parser.add_argument(
        "Variance",
        action="store",
        widget="Dropdown",
        nargs="*",
        choices=["Levene", "Brown-Forsythe"],
        default="Levene",
        help="Which variance tests to use",
    )
    universal_parser.add_argument(
        "Tests",
        action="store",
        widget="Dropdown",
        nargs="*",
        choices=["Kruskal-Wallis", "Mann-Whitney"],
        default="Kruskal-Wallis",
        help="Which statistical tests to use",
    )
    universal_parser.add_argument(
        "Post-hoc",
        action="store",
        widget="Dropdown",
        nargs="*",
        choices=["Dunn", "Tukey"],
        default="Dunn",
        help="Which post hoc tests to use",
    )
    which_paradigms = universal_parser.add_mutually_exclusive_group()
    which_paradigms.add_argument(
        "--Run all available paradigms", action="store_true", help="Listed on the left"
    )
    which_paradigms.add_argument(
        "--Select paradigms", action="store_true", help="Use box on the right"
    )
    universal_parser.add_argument(
        "--Paradigms",
        action="store",
        widget="Listbox",
        nargs="*",
        choices=[
            "Number of Visits",
            "Number of Nosepokes",
            "Visit Duration",
            "Nosepoke Duration",
            "Time to All Corners",
            "Time to All Nosepokes",
            "Corner Preference",
            "Door Preference",
            "Zig-zags Visits",
            "Perimeter Visits",
            "Overtake Occurrences",
        ],
        help="Make multiple selections using Ctrl and Shift",
    )
    universal_parser.add_argument(
        "--Excluded Groups", action="store", help="Groups to exclude"
    )
    universal_parser.add_argument(
        "--Excluded Animals", action="store", help="Animals to exclude"
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
            "--Data Directory",
            action="store",
            widget="DirChooser",
            help="Input directory containing Intellicage files",
        )
        paradigm_parser.add_argument(
            "--Output Directory",
            action="store",
            widget="DirChooser",
            help="Output directory to save analysis",
        )
        paradigm_parser.add_argument(
            "--Start",
            action="store",
            widget="DateChooser",
            help="Start times and dates of the phases",
        )
        paradigm_parser.add_argument(
            "--End",
            action="store",
            widget="DateChooser",
            help="End times and dates of the phases",
        )
        paradigm_parser.add_argument(
            "--Comparisons",
            action="store",
            widget="Dropdown",
            nargs="*",
            choices=["Between Group", "Within Group"],
            help="What comparisons to make",
        )
        paradigm_parser.add_argument(
            "--Error",
            action="store",
            widget="Dropdown",
            nargs="*",
            choices=["SEM", "SD"],
            help="Way error should be measured",
        )
        paradigm_parser.add_argument(
            "--Normality",
            action="store",
            widget="Dropdown",
            nargs="*",
            choices=["Shapiro–Wilk", "Kolmogorov–Smirnov"],
            help="Which normality tests to use",
        )
        paradigm_parser.add_argument(
            "--Variance",
            action="store",
            widget="Dropdown",
            nargs="*",
            choices=["Levene", "Brown-Forsythe"],
            help="Which variance tests to use",
        )
        paradigm_parser.add_argument(
            "--Tests",
            action="store",
            widget="Dropdown",
            nargs="*",
            choices=["Kruskal-Wallis", "Mann-Whitney"],
            help="Which statistical tests to use",
        )
        paradigm_parser.add_argument(
            "--Post-hoc",
            action="store",
            widget="Dropdown",
            nargs="*",
            choices=["Dunn", "Tukey"],
            help="Which post hoc tests to use",
        )
        paradigm_parser.add_argument(
            "--Plots",
            action="store",
            widget="Listbox",
            nargs="*",
            choices=["Bar", "Line"],
            help="Types of plots to make",
        )
        paradigm_parser.add_argument(
            "--Tables",
            action="store",
            widget="Listbox",
            nargs="*",
            choices=["Normality", "Variance", "Post-hoc"],
            help="Types of tables to make",
        )
        paradigm_parser.add_argument(
            "--Excluded Groups", action="store", help="Groups to exclude"
        )
        paradigm_parser.add_argument(
            "--Excluded Animals", action="store", help="Animals to exclude"
        )

    return parser.parse_args()


if __name__ == "__main__":
    conf = parse_args()
    us.create_project_layout(
        conf.data_directory, conf.output_directory, conf.project_name
    )
    us.create_notebook(
        conf.data_directory,
        conf.output_directory,
        conf.project_name,
        conf.paradigms,
        conf.start,
        conf.end,
        conf.excluded_groups,
        conf.excluded_animals,
        conf.comparisons,
        conf.error,
        conf.normality,
        conf.variance,
        conf.tests,
        conf.post_hoc,
        conf.plots,
        conf.tables,
    )
    print("Done")
