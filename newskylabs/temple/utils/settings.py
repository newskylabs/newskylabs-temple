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

"""newskylabs/temple/utils/settings.py:

Utilities to manage project settings.

"""

## =========================================================
## merge_settings()
## ---------------------------------------------------------

def merge_settings(defaults, overwrite):
    """Recursively merge 'overwrite' settings into the 'default' settings.

    In the case of settings which are defined in both, the settings
    given in 'overwrite' overwrite the 'default' settings.

    The function is destructive: the original values are reused and
    thereby manipulated by the function.

    Parameters
    ----------
    defaults
        The default settings.
    overwrite
        The overwrite settings.

    Returns
    -------
    The merged settings.

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
