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

"""newskylabs/temple/templates/engine.py

Definition of class TemplateEngine.

"""

import os
import sys

from pathlib import Path
from datetime import datetime

from newskylabs.temple.templates.jinja import generate_file_from_template
from newskylabs.utils.generic import get_recursively
from newskylabs.temple.utils.string_utilities import hyphen_to_underscore_in_keys, \
    hyphen_to_underscore

## =========================================================
## Exceptions
## ---------------------------------------------------------

class TempleException(Exception):
    """Base class for temple exceptions."""
    pass

class UndefinedProjectTypeError(TempleException):
    """Exception raised when the user provides an undefined project type.

    Attributes:
        projecttype -- the project type provided by the user
        message -- explanation of the error
    """

    def __init__(self, projecttype, message):
        self.projecttype = projecttype
        self.message     = message

## =========================================================
## Template engine
## ---------------------------------------------------------

class TemplateEngine():
    """
    """

    def __init__(self, project_type, project_name, settings):
        """
        """

        self._project_name = project_name
        self._settings     = settings

        # Variables for jinja2
        variables = settings.get_settings()
        self._variables = variables

        # Check that the project type is valid
        if not self.templates_defined(project_type):

            # Throw an error
            # in the case of undefined project types
            msg = "No templated defined for project type '{}'.".format(project_type)
            raise UndefinedProjectTypeError(project_type, msg)
        
        # Convenience alias defintions
        variables['author']['name'] = \
            '{} {}'.format(variables['author']['first-name'],
                           variables['author']['family-name'])

        variables['project'] = {
            'name': project_name,
            'language': variables[project_type]['language'],
        }

        variables['date'] = '{:%Y/%m/%d}'.format(datetime.now())
        variables['datetime'] = {
            'year':  '{:%Y}'.format(datetime.now()),
            'month': '{:%m}'.format(datetime.now()),
            'day':   '{:%d}'.format(datetime.now()),
        }
        
        variables['copyright'] = 'Copyright {} {}'\
            .format(variables['datetime']['year'],
                    variables['author']['name'])

        # Convert hyphens to underscores
        # to faciliate usage of variables in the jinja2 templates
        variables = hyphen_to_underscore_in_keys(variables)
        self._project_type = hyphen_to_underscore(project_type)
        self._variables = variables

    def templates_defined(self, project_type):
        """
        """
        settings = self._settings.get_settings()
        return (project_type in settings.keys() \
                and isinstance(settings[project_type], dict) \
                and 'template-dir' in settings[project_type].keys())

    def get_setting(self, variable):
        """Retrive a variable"""

        # When defined use the user settings
        value = get_recursively(_settings, keychain)
        if value != None:
            return value

        # When the user has not overwritten a setting use the default
        # settings
        value = get_recursively(_default_settings, keychain)
        if value != None:
            return value

            # When a setting has neither been defined in the user settings nor
            # in the default settings return None
        else:
            return None

    def generate(self, verbose=True, debug=False):
        """Generate a project of the given project type...
        """
        
        # Get settings
        # corresponding to the given project type
        project_variables = self._variables[self._project_type]
        project_name      = self._project_name
        variables         = self._variables

        template_dir = project_variables[hyphen_to_underscore('template-dir')]
        project_dir  = project_variables[hyphen_to_underscore('project-dir')]

        # Get the template base path
        template_base_path = Path(template_dir).expanduser().resolve()
        
        # Check that the template directory exists
        if not template_base_path.exists():
            print("ERROR The template directory '{}' does not exist!\n".format(template_dir))
            sys.exit(-1)

        # Calculate the project base path
        project_base_path = (
            Path(project_dir).expanduser().resolve() /
                 '{}'.format(project_name) /
                 '{}.git'.format(project_name))

        # Check if the project directory exists already 
        # (either in form of a file or as a directory)
        # If inform user 
        # and exit to avoid overwriting of existing files
        if project_base_path.exists():
            print('ERROR The path {} exists already!\n'.format(project_base_path) +
                  'Exiting to avoid overwriting of existing files.')
            sys.exit(-1)

        # Print a header
        print("\n"
              "Generating Python project '{}'...\n".format(project_name) +
              "\n"
              "  - template dir: {}\n".format(template_base_path) +
              "  - project dir:  {}\n".format(project_base_path))
        
        # INFO
        if verbose:
            print('mkdir -p {}'.format(project_base_path))
                
        # Create project base dir
        project_base_path.mkdir(parents=True, exist_ok=False)

        # Dirs and files to exclude
        exclude_dirs  = ['.git']
        exclude_files = []
        
        # Walk the templates...
        for template_path, directories, filenames in os.walk(template_base_path):
            
            # Skip the directories in the exclude list 
            directories[:] = [d for d in directories if d not in exclude_dirs]

            # Skip the files in the exclude list 
            filenames[:] = [f for f in filenames if f not in exclude_files]

            # Skip temporary files
            filenames[:] = [f for f in filenames 
                            if not (f[0] == '#' or 
                                    f[-1] == '~' or
                                    (len(f) >= 2 and f[:2] == '.#'))]

            # Calculate the relative path 
            # by "subtracting" the base path from the absolute path
            rel_path = os.path.relpath(template_path, template_base_path)
            project_path = os.path.abspath(os.path.join(project_base_path, rel_path))

            # DEBUG
            if debug:
                print('DEBUG\n'
                      '  - template_path: {}\n'.format(template_path) +
                      '  - rel_path:      {}\n'.format(rel_path) +
                      '  - project_path:  {}\n'.format(project_path) +
                      '  - directories:   {}\n'.format(directories) +
                      '  - filenames:     {}\n'.format(filenames))
            
            for directory in directories:

                # Resolve the paths
                template_dir = os.path.join(template_path, directory)
                project_dir = os.path.join(project_path, directory)

                # DEBUG
                if debug:
                    print('DEBUG\n'
                          '  - template_dir: {}\n'.format(template_dir) +
                          '  - project_dir:  {}\n'.format(project_dir))

                # INFO
                if verbose:
                    print('mkdir {}'.format(project_dir))
                
                # Create the corresponding project directory
                os.mkdir(project_dir)

            for filename in filenames:

                # Resolve the paths
                template_file = os.path.join(template_path, filename)
                project_file = os.path.join(project_path, filename)

                # DEBUG
                if debug:
                    print('DEBUG\n'
                          '  - template_file: {}\n'.format(template_file) +
                          '  - project_file:  {}\n'.format(project_file))

                # Generate the corresponding file from the template
                generate_file_from_template(project_file, template_file, variables,
                                            verbose=verbose, debug=debug)

## =========================================================
## =========================================================

## fin.
