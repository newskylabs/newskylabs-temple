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

"""newskylabs/temple/utils/generic.py:

Generic utilities...

"""

## =========================================================
## Utilities for python dictionaries
## ---------------------------------------------------------

def set_recursively(structure, path, value):
    """Set a value in a recursive structure."""

    path = path.split('.')
    lastkey = path.pop()

    for key in path:
        if not key in structure or not isinstance(structure[key], dict):
            structure[key] = {}
        structure = structure[key]

    structure[lastkey] = value
    
def get_recursively(structure, keychain):
    """Get a value from a recursive structure."""

    val = structure

    # Follow the key chain to recursively find the value
    for key in keychain.split('.'):
        if isinstance(val, dict) and key in val:
            val = val[key]
        elif key.isdigit() and isinstance(val, list) and int(key) < len(val):
            val = val[int(key)]
        else:
            return None

    return val

## =========================================================
## merge_settings()
## ---------------------------------------------------------

def merge_settings(defaults, overwrite):
    """Recursively overwrite the default settings with the overwrite
    settings.

    Note that the function is destructive: the dictionaries passed
    into the functions as parameters are reused for building the
    merged setting dictionary.

    """

    if isinstance(overwrite, dict) \
       and isinstance(defaults, dict):
        # When overwrite is a dictionary
        # and defaults as well
            
        # Start from the defaults
        merged = defaults

        # And merge in the overwritten settings
        for key, value in overwrite.items():
            
            if key in defaults:
                # Recursively merge the values of keys 
                # exising in both: defaults and overwrite
                merged[key] = merge_settings(merged[key], value)
                
            else:
                # Extend the settings with new settings 
                # only defined in the 'overwrite' settings
                merged[key] = value

    else:
        # In all other cases the 'overwrite' settings
        # are used
        merged = overwrite

    return merged

## =========================================================
## =========================================================

## fin.
