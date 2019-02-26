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
## =========================================================

## fin.
