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
        description="Tools to aid Intellicage analysis using PyMICE"
    )

    subs = parser.add_subparsers()
    num_vists_parser = subs.add_parser("Number of Visits")
    num_nosepokes_parser = subs.add_parser("Number of Nosepokes")
    visit_dur_parser = subs.add_parser("Visit Duration")
    nosepoke_dur_parser = subs.add_parser("Nosepoke Duration")
    time_to_corners_parser = subs.add_parser("Time to All Corners")
    time_to_nosepokes_parser = subs.add_parser("Time to All Nosepokes")
    corner_preference_parser = subs.add_parser("Corner Preference")
    door_preference_parser = subs.add_parser("Door Preference")
    zig_zag_parser = subs.add_parser("Zig-zags")
    perimeter_parser = subs.add_parser("Perimeter Visits")
    overtake_occurrences = subs.add_parser("Overtake Occurrences")

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
