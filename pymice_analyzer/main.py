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


@gy.Gooey(
    program_name="PyMICE Analyzer",
    tabbed_groups=True,
    dump_build_config=True,
    load_build_config=None,
)
def parse_args():
    """Use GooeyParser to build up arguments in the script and save the arguments in a
    default json file so that they can be retrieved each time the script is ran.
    """
    parser = gy.GooeyParser(
        description="Tools to aid Intellicage analysis using PyMICE"
    )

    universal_group = parser.add_argument_group(
        "Universal Settings",
        "Settings to be applied to all paradigms unless overridden",
    )
    num_vists_group = parser.add_argument_group("Number of Visits")
    num_pokes_group = parser.add_argument_group("Number of Nosepokes")
    visit_dur_group = parser.add_argument_group("Visit Duration")
    poke_dur_group = parser.add_argument_group("Nosepoke Duration")
    time_corners_group = parser.add_argument_group("Time to All Corners")
    time_pokes_group = parser.add_argument_group("Time to All Nosepokes")
    corner_pref_group = parser.add_argument_group("Corner Preference")
    door_pref_group = parser.add_argument_group("Door Preference")
    zig_zag_group = parser.add_argument_group("Zig-zag Visits")
    perimeter_group = parser.add_argument_group("Perimeter Visits")
    overtake_group = parser.add_argument_group("Overtake Occurrences")

    universal_group.add_argument(
        "Project Name", action="store", help="Name of your project"
    )
    universal_group.add_argument(
        "Run pipeline after generating scripts?",
        action="store",
        widget=("CheckBox"),
        help="   If unchecked, use 'run-all.py' in project directory.",
    )
    universal_group.add_argument(
        "Data Directory",
        action="store",
        widget="DirChooser",
        help="Input directory containing Intellicage files",
    )
    universal_group.add_argument(
        "Output Directory",
        action="store",
        widget="DirChooser",
        help="Output directory to save analysis",
    )
    universal_group.add_argument(
        "-s",
        "--Start (optional)",
        action="store",
        widget="DateChooser",
        help="Start times and dates of the phases",
    )
    universal_group.add_argument(
        "-e",
        "--End (optional)",
        action="store",
        widget="DateChooser",
        help="End times and dates of the phases",
    )

    # paradigm_list = [
    #     num_vists_parser,
    #     num_nosepokes_parser,
    #     visit_dur_parser,
    #     nosepoke_dur_parser,
    #     time_to_corners_parser,
    #     time_to_nosepokes_parser,
    #     corner_preference_parser,
    #     door_preference_parser,
    #     zig_zag_parser,
    #     perimeter_parser,
    #     overtake_occurrences,
    # ]
    #
    # universal_settings_parser.add_argument(
    #     "Data Directory",
    #     action="store",
    #     widget="DirChooser",
    #     help="Input directory containing Intellicage files",
    # )
    # universal_settings_parser.add_argument(
    #     "Output Directory",
    #     action="store",
    #     widget="DirChooser",
    #     help="Output directory to save analysis",
    # )
    # universal_settings_parser.add_argument(
    #     "Start",
    #     action="store",
    #     widget="DateChooser",
    #     help="Start times and dates of the phases",
    # )
    # universal_settings_parser.add_argument(
    #     "End",
    #     action="store",
    #     widget="DateChooser",
    #     help="End times and dates of the phases",
    # )
    #
    # for paradigm in paradigm_list:
    #     paradigm.add_argument(
    #         "-eg", "--Excluded Groups", action="store", help="Groups to exclude"
    #     )
    #     paradigm.add_argument(
    #         "-ea", "--Excluded Animals", action="store", help="Animals to exclude"
    #     )

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
