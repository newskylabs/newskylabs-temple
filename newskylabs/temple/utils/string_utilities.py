## =========================================================
## Copyright 2019 Dietrich Bollmann
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##      http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## ---------------------------------------------------------

"""newskylabs/temple/utils/string_utilities.py:

String utilities.

"""

## =========================================================
## hyphen_to_underscore_string()
## ---------------------------------------------------------

def hyphen_to_underscore_string(string):
    """
    Convert hyphens to underscores in the given string
    """
    return string.replace('-', '_')

## =========================================================
## Utility functions
## ---------------------------------------------------------

def _hyphen_to_underscore(obj):
    """
    Convert hyphens to underscores in the keys of dictionaries.
    """

    if isinstance(obj, dict):
        return _hyphen_to_underscore_dict(obj)

    elif isinstance(obj, list):
        return _hyphen_to_underscore_list(obj)

    elif isinstance(obj, tuple):
        return _hyphen_to_underscore_tuple(obj)

    else:
        return obj

def _hyphen_to_underscore_dict(dictionary):
    """
    Convert hyphens to underscores in the keys of dictionaries.
    """

    target = dict()
    for key, value in dictionary.items():

        key = key.replace('-', '_')

        target[key] = _hyphen_to_underscore(value)

    return target

def _hyphen_to_underscore_list(l):
    """
    Convert hyphens to underscores in the keys of dictionaries.
    """
    return [_hyphen_to_underscore(item) for item in l]

def _hyphen_to_underscore_tuple(t):
    """
    Convert hyphens to underscores in the keys of dictionaries.
    """
    return tuple(_hyphen_to_underscore_list(t))

## =========================================================
## hyphen_to_underscore_in_keys()
## ---------------------------------------------------------

def hyphen_to_underscore_in_keys(dictionary):
    """
    Convert hyphens to underscores in the keys of dictionaries.
    """
    return _hyphen_to_underscore_dict(dictionary)

## =========================================================
## =========================================================

## fin.
