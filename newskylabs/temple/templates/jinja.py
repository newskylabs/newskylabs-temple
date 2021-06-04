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

"""newskylabs/temple/templates/jinja.py:

Jinja utilities for generating files from templates using jinja2.

"""

import os, sys
from jinja2 import Template, Environment, FileSystemLoader

from newskylabs.temple.templates.filters.markdown import markdown_filter
from newskylabs.temple.templates.filters.latex    import latex_filter
from newskylabs.temple.templates.filters.html     import html_filter
from newskylabs.temple.templates.filters.html_paragraphs import html_paragraph_filter

## =========================================================
## jinja tools
## ---------------------------------------------------------

def read_template(template_path, variables):
    """
    """

    # Get filename and extension
    filename, file_extension = os.path.splitext(template_path)

    # Get rid of the leading '.'
    # Ex: '.html' -> 'html'
    if len(file_extension) > 0 and file_extension[0] == '.':
        file_extension = file_extension[1:] 
    
    # Simplest version to generate a file from a template:
    # 
    #| with open(template_path) as fh: # Use file to refer to the file object
    #|     template_str = fh.read()
    #|     
    #| template = Template(template_str)
    # 
    # However, here I am generating the template from a Jinja2 Environment
    # as this allows for more customization:

    # Jinja2 extensions
    jinja_extensions = [
        # Expression Statement Extension
        # http://jinja.pocoo.org/docs/2.10/extensions/#expression-statement
        # 
        # The “do” aka expression-statement extension adds a
        # simple do tag to the template engine that works like a
        # variable expression but ignores the return value.
        # 
        # Example: 
        # 
        #   {% do navigation.append('a string') %}
        # 
        'jinja2.ext.do',
    ]
    
    # Am I rendering a LaTeX file?
    #| if template_path[-4:].lower() == '.tex' or \
    #|    template_path[-4:].lower() == '.sty':
    if template_path[-4:].lower() == '.tex':

        # LaTeX files
        language = 'latex'

        # When rendering LaTeX files
        # use the following delimiters:
        # 
        #   <% ... %> for Statements
        #   << ... >> for Expressions to print to the template output
        #   <# ... #> for Comments not included in the template output
        #
        env = Environment(
            loader                = FileSystemLoader(os.path.dirname(template_path)), 
            block_start_string    = '<%', block_end_string    = '%>',
            variable_start_string = '<<', variable_end_string = '>>',
            comment_start_string  = '<#', comment_end_string  = '#>',
            keep_trailing_newline = True, # Keep newline at end of template
            trim_blocks           = True, # Remove first newline after block
            extensions            = jinja_extensions,
        )

    else:
        # 
        # Not a LaTeX files
        # 
        # In all other cases 
        # use the default jinja2 delimiters:
        # 
        #   {% ... %} for Statements
        #   {{ ... }} for Expressions to print to the template output
        #   {# ... #} for Comments not included in the template output
        # 
        env = Environment(
            loader                = FileSystemLoader(os.path.dirname(template_path)), 
            keep_trailing_newline = True, # Keep newline at end of template
            trim_blocks           = True, # Remove first newline after block
            extensions            = jinja_extensions,
        )

    # Add the file extension to the variables
    variables['temple'] = {
        'template': {
            'file_extension': file_extension,
        },
    }

    # Add data required by templs
    env.temple = {
        'variables': variables,
    }

    # Add filters
    env.filters['markdown']        = markdown_filter
    env.filters['latex']           = latex_filter
    env.filters['html']            = html_filter
    env.filters['html_paragraphs'] = html_paragraph_filter
    
    template = env.get_template(os.path.basename(template_path))

    return template

def save_file(file_path, content):
    """
    """
    with open(file_path, "w") as fh:
        fh.write(content)

def jinja(filename, template, variables):
    """
    """

    templateobj = read_template(template, variables)

    rendered_template = templateobj.render(**variables)

    # DEBUG
    #| print('DEBUG rendered_template:', rendered_template)

    save_file(filename, rendered_template)

def jinja_str(template_str, variables):
    """Render a template string with Jinja2 using the given variables.
    """
    template = Template(template_str)
    rendered_str = template.render(**variables)

    return rendered_str

## =========================================================
## generate_file_from_template()
## ---------------------------------------------------------

def generate_file_from_template(filename, template, variables, 
                                verbose=False, debug=False):
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
