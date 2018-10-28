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

"""Load and clean data from Intellicage."""


import pymice as pm


def load_data(*args, **kwargs):
    """Loads the data and checks its validity."""
    data_files = [0 for x in range(len(args))]
    for i in range(0, len(args)):
        data_files[i] = args[i]

    # Merge the data.
    loaders = [pm.Loader(filename) for filename in data_files]
    data = pm.Merger(*loaders)
    print("Done loading data.")
    for mouse in sorted(data.getGroup()):
        print(mouse)

    # Read in period of analysis from timeline.ini.
    timeline = pm.Timeline("../timeline/hab1.ini")
    start1, end1 = timeline.getTimeBounds(kwargs["phase1"])
    start2, end2 = timeline.getTimeBounds(kwargs["phase2"])
    print("%s:\t%s - %s" % (kwargs["phase1"], start1, end1))
    print("%s:\t%s - %s" % (kwargs["phase2"], start2, end2))

    # Check for any problems (indicated in the log) during the period of interest.
    data_validator = pm.DataValidator(pm.PresenceLogAnalyzer())
    validator_report = data_validator(data)
    no_presence_problems = pm.FailureInspector("Presence")
    if no_presence_problems(validator_report, (start1, end1)):
        if no_presence_problems(validator_report, (start2, end2)):
            print("Presences OK.")

    return data, start1, end1, start2, end2
