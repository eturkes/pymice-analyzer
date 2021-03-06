#!/usr/bin/env python3
# -*- coding: utf-8 -*

#    This file is part of pymice-analyzer.
#    Copyright (C) 2018-2020  Emir Turkes, Phenovance LLC
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
#    Emir Turkes can be contacted at emir.turkes@eturkes.com

"""Miscellaneous methods to help with the main routine."""


import configparser as cp
import os
import shutil as sl

import nbformat as nbf
import git


def create_project_layout(data_dir, proj_path):
    """Creates layout of project directories."""
    os.makedirs(os.path.join(proj_path, "pipeline"))
    os.mkdir(os.path.join(proj_path, "pipeline", "timeline"))
    os.mkdir(os.path.join(proj_path, "data"))
    os.mkdir(os.path.join(proj_path, "output"))
    os.symlink(data_dir, os.path.join(proj_path, "data", "intellicage"))
    sl.copy2(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "misc",
            "docker-jupyter-notebook.sh",
        ),
        os.path.join(proj_path, "docker-jupyter-notebook.sh"),
    )
    git.Repo.clone_from(
        "https://github.com/eturkes/pymice-modules",
        os.path.join(proj_path, "pipeline", "pymice-modules"),
    )
    sl.move(
        os.path.join(proj_path, "pipeline", "pymice-modules", "pymice_modules"),
        os.path.join(proj_path, "pipeline", "modules"),
    )
    sl.copy2(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "misc", "update_modules.sh"
        ),
        os.path.join(proj_path, "pipeline", "modules"),
    )
    sl.rmtree(os.path.join(proj_path, "pipeline", "pymice-modules"))


def create_timeline(start, end, tzinfo, proj_path):
    """Creates timeline INI file."""
    conf = cp.ConfigParser()
    conf.add_section("Phase 1")
    conf["Phase 1"]["start"] = start
    conf["Phase 1"]["end"] = end
    conf["Phase 1"]["tzinfo"] = tzinfo
    with open(
        os.path.join(proj_path, "pipeline", "timeline", "timeline.ini"), "w"
    ) as file:
        conf.write(file)


def create_notebook(
    all_paradigms,
    data_dir,
    proj_path,
    proj_name,
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
    # Get only the last part of data_dir for loading data later.
    rel_data_dir = os.path.join(
        "..", "data", os.path.basename(os.path.normpath(data_dir))
    )

    for paradigm in all_paradigms:
        notebook = nbf.v4.new_notebook()

        cell_0 = f"""\
# {all_paradigms[paradigm]} - {proj_name}"""

        cell_1 = """
## Run Paradigm"""

        cell_2 = f"""\
# Input arguments.
start = ("{start}")
end = ("{end}")
excluded_groups = ("{excluded_groups}")
excluded_animals = ("{excluded_animals}")

# Main routine.
import glob
import modules.utils.import_all
import modules.utils.load_data
modules.utils.import_all.import_all(
    "modules/utils", globals()
)
modules.utils.import_all.import_all(
    "modules/paradigms", globals()
)
modules.utils.import_all.import_all(
    "modules/stats", globals()
)
modules.utils.import_all.import_all(
    "modules/display", globals()
)

data, start, end = modules.utils.load_data.load_data(
    glob.glob("../../intellicage/*.zip"), 
    start=start,
    end=end,
)"""

        cell_3 = """\
## Statistical Testing"""

        cell_4 = f"""\
# Input arguments.
comparisons = ("{comparisons}")
error = ("{error}")
normality = ("{normality}")
variance = ("{variance}")
tests = ("{tests}")
post_hoc = ("{post_hoc}")

# Main routine."""

        cell_5 = """\
## Generate Figures"""

        cell_6 = f"""\
# Input arguments.l
plots = ("{plots}")
tables = ("{tables}")

# Main routine."""

        notebook["cells"] = [
            nbf.v4.new_markdown_cell(cell_0),
            nbf.v4.new_markdown_cell(cell_1),
            nbf.v4.new_code_cell(cell_2),
            nbf.v4.new_markdown_cell(cell_3),
            nbf.v4.new_code_cell(cell_4),
            nbf.v4.new_markdown_cell(cell_5),
            nbf.v4.new_code_cell(cell_6),
        ]

        pipeline_dir = os.path.join(proj_path, "pipeline")
        notebook_file_name = all_paradigms[paradigm].lower().replace(" ", "_")
        nbf.write(notebook, f"{os.path.join(pipeline_dir, notebook_file_name)}.ipynb")
