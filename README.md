<!---
    pymice-analyzer
    Copyright (C) 2018  Emir Turkes

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Emir Turkes can be contacted at eturkes@bu.edu
-->

# PyMICE Analyzer

Tools to expand the functionality of [PyMICE](https://github.com/Neuroinflab/PyMICE)

# Example INI file

[Total Events]  
data = ../data/comp+old-behav-flex  
start = 2017-03-20 11:02:07, 2017-03-21 11:02:07  
end = 2017-03-20 12:02:07, 2017-03-22 09:02:07  
excluded-groups = Cage9 Pump  
excluded-animals = 19 WT, 13 KO  
cages = 2  

events = visits, nosepokes  
error = SEM  
comparisons = between-group, within-group  
normality = shapiro  
variance = levene  
stats = kruskal-wallis  
post-hoc = dunns  

bar-graph = post-hoc  
graph-settings = combined-plots  
table = normality, variance, post-hoc  
table-settings = combined-plots  
