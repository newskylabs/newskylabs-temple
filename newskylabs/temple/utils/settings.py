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

import errno
import os
import yaml

from newskylabs.temple.utils.generic import set_recursively, get_recursively

## =========================================================
## Class Settings
## ---------------------------------------------------------

class Settings:
    """A simple class to manage project settings"""

    def __init__(self, default_settings_file, user_settings_file):
        """
        """
        self.init_settings(default_settings_file, user_settings_file)
        
    def init_settings(self, default_settings_file, user_settings_file):
        """
        """
        
        # Throw an error
        # when no default_settings file has been given
        if default_settings_file == None:
            raise TypeError(
                errno.ENOENT, "A default settings file has to be given!")
        
        # Throw an error
        # when the default_settings file does not exist
        if not os.path.isfile(default_settings_file):
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), default_settings_file)
        
        # Load the default settings
        default_settings = self.load_settings_file(default_settings_file)

        if user_settings_file == None \
            or not os.path.isfile(user_settings_file):
            # No user settings file given - use the defaults
            self._settings = default_settings
    
        else:
            # Load the user settings
            # and use them to overwrite the defaults
            user_settings = self.load_settings_file(user_settings_file)
            self._settings = self.merge_settings(default_settings, user_settings)

    @staticmethod
    def load_settings_file(settings_file):
        """Load a yaml settings file"""
            
        if os.path.isfile(settings_file):
            with open(settings_file, 'r') as fh:
                return yaml.load(fh)
        else:
            return None

    @staticmethod
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
                    merged[key] = Settings.merge_settings(merged[key], value)
                
                else:
                    # Extend the settings with new settings 
                    # only defined in the 'overwrite' settings
                    merged[key] = value

        else:
            # In all other cases the 'overwrite' settings
            # are used
            merged = overwrite

        return merged

    def get_settings(self):
        """Retrive the dictionary with all settings."""
    
        return self._settings

    def set_setting(self, keychain, value):
        """Set a setting."""
    
        set_recursively(self._settings, keychain, value)
    
    def get_setting(self, keychain):
        """Retrive a setting"""
    
        return get_recursively(self._settings, keychain)

## =========================================================
## =========================================================

## fin.
