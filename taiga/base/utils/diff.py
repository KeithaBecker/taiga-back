# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


def make_diff(first:dict, second:dict, not_found_value=None) -> dict:
    """
    Compute a diff between two dicts.
    """
    diff = {}

    # Check all keys in first dict
    for key in first:
        if key not in second:
            diff[key] = (first[key], not_found_value)
        elif first[key] != second[key]:
            diff[key] = (first[key], second[key])

    # Check all keys in second dict to find missing
    for key in second:
        if key not in first:
            diff[key] = (not_found_value, second[key])

    return diff
