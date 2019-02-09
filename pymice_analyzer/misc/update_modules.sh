#!/bin/sh

#    This file is part of pymice-analyzer.
#    Copyright (C) 2018-2019  Emir Turkes
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

# Git pulls the latest pymice-modules
# If local modifications were made, move append modified files with .old and move into
# new directory

cd ..
mv modules modules.old
git clone https://github.com/eturkes/pymice-modules
mv pymice-modules/pymice_modules modules
mv modules.old/update_modules.sh modules
rm -Rf pymice-modules

# The following section is adapted from content on Stack Overflow
# https://stackoverflow.com/questions/6765054/shell-script-to-compare-directories-recursively
# Question asked by: Brandon https://stackoverflow.com/users/841185/brandon
# Answer given by: Manny D https://stackoverflow.com/users/771329/manny-d
# START adapted content
OLD_IFS=$IFS
# The extra space after is crucial
IFS=\ 

for old_file in `diff -rq modules.old/ modules/ | grep "^Files.*differ$" \
    | sed 's/^Files \(.*\) and .* differ$/\1/'`
do
    old_ext=$old_file.old
    mv $old_file $old_ext
    new_path=${old_ext//modules.old/modules}
    mv $old_ext $new_path
    echo Created $new_path
done
IFS=$OLD_IFS
# END adapted content

rm -Rf modules.old
