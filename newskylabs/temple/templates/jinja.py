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

"""newskylabs/temple/utils/jinja.py:

Jinja utilities for generating files from templates using jinja2.

"""

from jinja2 import Template

## =========================================================
## jinja tools
## ---------------------------------------------------------

def read_template(template_path):
    """
    """

    with open(template_path) as fh: # Use file to refer to the file object
        template_str = fh.read()

    template = Template(template_str)

    return template

def save_file(file_path, content):
    """
    """
    with open(file_path, "w") as fh:
        fh.write(content)

def jinja(filename, template, variables):
    """
    """

    templateobj = read_template(template)

    rendered_template = templateobj.render(**variables)

    # Add a newline character
    rendered_template += '\n'

    # DEBUG
    #| print('DEBUG rendered_template:', rendered_template)

    save_file(filename, rendered_template)

## =========================================================
## generate_file_from_template()
## ---------------------------------------------------------

def generate_file_from_template(filename, template, variables, verbose=False, debug=False):
    """
    """
    
    # DEBUG
    if debug:
        print('DEBUG generate_file_from_template():\n'
              '  - filename:  {}\n'.format(filename) +
              '  - template:  {}\n'.format(template) +
              '  - variables: {}\n'.format(variables))
                
    # INFO
    if verbose:
        print('jinja {}'.format(filename))
                
    # Generate the file from the template
    jinja(filename, template, variables)

## =========================================================
## =========================================================

## fin.
