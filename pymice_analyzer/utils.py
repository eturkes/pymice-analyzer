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

"""Miscellaneous methods to help with the main routine."""


import os
import shutil as sl

import nbformat as nbf


def create_project_layout(data_directory, output_directory, project_name):
    """Creates layout of project directories"""
    os.makedirs(os.path.join(output_directory, project_name, "pipeline"))
    os.mkdir(os.path.join(output_directory, project_name, "data"))
    os.mkdir(os.path.join(output_directory, project_name, "output"))
    os.symlink(
        data_directory,
        os.path.join(output_directory, project_name, "data", "intellicage"),
    )
    sl.copytree(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules"),
        os.path.join(output_directory, project_name, "pipeline", "modules"),
    )


def create_notebook():
    """Produces a Jupyter Notebook .ipynb file."""
    nb = nbf.v4.new_notebook()

    cell_0 = """\
    # Number of Visits - Project Name"""

    cell_1 = """\
    # Load modules necessary for the notebook to run.
    import modules.importdir
    importdir.do("modules", globals())"""

    cell_2 = """\
    ## Run Paradigm"""

    cell_3 = """\
    # Tweakable constants.
    START = ["2017-03-20 11:02:07", "2017-03-21 11:02:07"]
    END = ["2017-03-20 12:02:07", "2017-03-22 09:02:07"]
    EXCLUDED_GROUPS = ["Cage9 Pump"]
    EXCLUDED_ANIMALS = ["19 WT", "13 KO"]
    
    # Main routine."""

    cell_4 = """\
    ## Statistical Testing"""

    cell_5 = """\
    # Tweakable constants.
    COMPARISONS = ["between_group", "within_group"]
    ERROR = ["sem"]
    NORMALITY = ["shapiro"]
    VARIANCE = ["levene"]
    METHOD = ["kruskal_wallis"]
    POST_HOC = ["dunns"]
    
    # Main routine."""

    cell_6 = """\
    ## Generate Figures"""

    cell_7 = """\
    # Tweakable constants.
    PLOTS = ["bar"]
    TABLES = ["normality", "variance", "post_hoc"]
    
    # Main routine."""

    nb["cells"] = [
        nbf.v4.new_markdown_cell(cell_0),
        nbf.v4.new_code_cell(cell_1),
        nbf.v4.new_markdown_cell(cell_2),
        nbf.v4.new_code_cell(cell_3),
        nbf.v4.new_markdown_cell(cell_4),
        nbf.v4.new_code_cell(cell_5),
        nbf.v4.new_markdown_cell(cell_6),
        nbf.v4.new_code_cell(cell_7),
    ]

    nbf.write(nb, "number_of_visits.ipynb")
