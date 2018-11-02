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


def create_project_layout(data_dir, out_dir, proj_name):
    """Creates layout of project directories"""
    os.makedirs(os.path.join(out_dir, proj_name, "pipeline"))
    os.mkdir(os.path.join(out_dir, proj_name, "pipeline", "timeline"))
    os.mkdir(os.path.join(out_dir, proj_name, "data"))
    os.mkdir(os.path.join(out_dir, proj_name, "output"))
    os.symlink(data_dir, os.path.join(out_dir, proj_name, "data", "intellicage"))
    sl.copytree(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules"),
        os.path.join(out_dir, proj_name, "pipeline", "modules"),
    )
    sl.copy2(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "misc", "inspect-pipeline.sh"
        ),
        os.path.join(out_dir, proj_name, "inspect-pipeline.sh"),
    )
    sl.copy2(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "misc", "1-min-bin.sh"
        ),
        os.path.join(out_dir, proj_name, "pipeline", "timeline", "1-min-bin.sh"),
    )


def create_notebook(
    data_directory,
    output_directory,
    project_name,
    paradigms,
    start,
    end,
    excluded_groups,
    excluded_animals,
    comparisons,
    error,
    normality,
    variance,
    tests,
    post_hoc,
    plots,
    tables,
):
    """Produces a Jupyter Notebook .ipynb file."""
    nb = nbf.v4.new_notebook()

    cell_0 = f"""\
    # {paradigms} - {project_name}"""

    cell_1 = """\
    # Load modules necessary for the notebook to run.
    import modules.importdir
    importdir.do("modules", globals())"""

    cell_2 = """\
    ## Run Paradigm"""

    cell_3 = f"""\
    # Input arguments.
    start = ("{start}")
    end = ("{end}")
    excluded_groups = ("{excluded_groups}")
    excluded_animals = ("{excluded_animals}")
    
    # Main routine."""

    cell_4 = """\
    ## Statistical Testing"""

    cell_5 = f"""\
    # Input arguments.
    comparisons = ("{comparisons}")
    error = ("{error}")
    normality = ("{normality}")
    variance = ("{variance}")
    tests = ("{tests}")
    post_hoc = ("{post_hoc}")
    
    # Main routine."""

    cell_6 = """\
    ## Generate Figures"""

    cell_7 = f"""\
    # Input arguments.
    plots = ("{plots}")
    tables = ("{tables}")
    
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

    nbf.write(nb, f"{project_name}.ipynb")
