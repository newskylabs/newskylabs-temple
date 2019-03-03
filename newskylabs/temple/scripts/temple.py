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

"""newskylabs/temple/scripts/temple.py:

Definition of the command line script `temple`.

"""

import click

from pathlib import Path

from newskylabs.temple.utils.settings import Settings
from newskylabs.temple.templates.engine \
    import TemplateEngine, UndefinedProjectTypeError

## =========================================================
## Entry point of console script 'temple'
## ---------------------------------------------------------

## =========================================================
## Group:
## ---------------------------------------------------------

@click.group(context_settings={'help_option_names': ['-h', '--help']})
# Version options: -V, --version
###@click.version_option(get_version_long(), '-V', '--version')
def cli():
    """
    temple - a simple tool to generate project sceletons from templates.
    """

## =========================================================
## Command: generate
## ---------------------------------------------------------

@cli.command(name="generate")
@click.argument('project_type', type=str)
@click.argument('project_name', type=str)
def command_generate(project_type, project_name):
    """Generate a python project with the given name.
    """

    # Get the directory of this file 
    this_dir = Path(__file__).parent;

    # Calculate the path of the default settings file
    default_settings_file = this_dir / 'default_settings.yaml'
    
    # Calculate the path of the user setting file
    user_settings_file = Path.home() / '.newskylabs/temple/settings.yaml'

    # Settings
    # The settings are calculated by 
    # overwriting the default settings with and the user settings
    settings = Settings(default_settings_file, user_settings_file)

    # Instantiate the TemplateEngine
    try:
        engine = TemplateEngine(project_type, project_name, settings)

        # Generate the project
        engine.generate()

    except UndefinedProjectTypeError as e:

        # Print error message
        # No templates defined for project type
        print('ERROR', e.message)
        sys.exit(1)

    finally:
        # Currently nothing to do here
        pass

    # Done
    print('')
    print('done.')
    print('')

## =========================================================
## =========================================================

## fin.
