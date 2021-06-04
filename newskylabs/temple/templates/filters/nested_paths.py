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

"""newskylabs/temple/templates/filters/nested_paths.py:

Utility functions to deal with <tmple /> tags containing nested jinja
paths.

TODO: Edit the following examples - some of them should be added to
the <temple /> tag function...

Examples:

Example context:

  email.private.tex:  some@email.address
  email.private.html: <a href="..." ...>...</a>

Example 1:

  <temple var="email.private.tex" />

  The variable 'email.private.tex' is looked up in the context and its
  value 'some@email.address' is substituted for the tag.

Example 2:

  <temple var="email.private.html" />

  The variable 'email.private.html' is looked up in the context and
  its value '<a href="..." ...>...</a>' is substituted for the tag.

Example 3:

  <temple var="temple.template.file-extension" />

  The variable 'temple.template.file-extension' is contains the
  extension of the template file: 'tex' in case of a latex template
  file, 'html' in case of an html template file.

  Therefore the tag is substituted with different values depending on
  the template file: In case of an html file the tag translates to
  'html', while for a latex file it will become 'tex'.

Example 4:

  <temple var="email.private.{temple.template.file-extension}" />

  First the nested path '{temple.template.file-extension}' is
  substituted with extension of the template file: 'tex' in case of a
  latex template file, 'html' in case of an html template file.

  Then the resulting path is looked up and substituted for the 
  <temple /> tag: In case of an html file the tag translates to 
  '<a href="..." ...>...</a>', while for a latex file it will 
  become 'some@email.address'.

More general examples:

  The <temple var="some.variable.path" /> tag allows to insert other path values.

  Example:

  Path setting:   email.private.txt: me@my.domain
  Template text:  'Email: <temple var="email.private.txt" />, Tel: 12345'
  Result:         'Email: me@my.domain, Tel: 12345'

  Paths can be nested:

  Example:

  Path settings:   
    email.private.txt:   me@my.domain
    adress-type:         private
    email.{adress-type}.txt:   me@my.domain
  Template text:  '<temple var="email.{adress-type}.txt" />'
  Result:         'Email: me@my.domain, Tel: 12345'

  Some special variables can be used:

  Example:

  The variable 'temple.template.file-extension' contains the file extension of the 
  current template file and can be used as follows:

  Template file:  template.txt
  Path settings:  email.private.txt: me@my.domain
  Template text:  '<temple var="email.private.{temple.template.file-extension}" />'
  Result:         'me@my.domain'

  Paths can be nested recursively:

  Example:  '<temple var="also.{{some.path}.{some.other.path}}.path" />'

  Path / Value definitions:

  'some.path'       -> 'another'
  'some.other.path' -> 'path'
  'another.path'    -> 'a'
  'also.a.path'     -> 'value'

  With these definitions the following recursive chain of substitutions will take place:

  '<temple var="also.{{some.path}.{some.other.path}}.path" />'
  '<temple var="also.{another.{some.other.path}}.path" />'
  '<temple var="also.{another.path}.path" />'
  '<temple var="also.a.path" />'
  'value'

"""

import sys, re

from newskylabs.utils.generic import get_recursively

## =========================================================
## get_path_value(variables, path)
## ---------------------------------------------------------

def _parse_path_string(variables, path):
    """
    Parse the longest prefix of 'path'
    made of any characters beyond '{' and '}'.
    """

    pattern = re.compile(r"([^{}]*)(.*)")
    match = pattern.match(path)
    if match:
        string = match.group(1)
        rest   = match.group(2)

        return string, rest

    else:
        # Should never happen
        raise Exception("_parse_path_string(): Unable to parse the path '{}'!".format(path))

def _parse_nested_path(variables, path):
    """Parse a nested path included in '{' and '}' and return its value.
    Nested paths are allowed to be recursive - a nested path might
    itself contain other nested paths.

    """

    # Read leading '{'
    if path[0] != '{':
        # Ill-formed path
        raise Exception("_parse_nested_path(): A nested path has to start with '{{': {}" \
                        .format(path))
    path = path[1:]

    # Parse the nested path 
    # and get its value
    value, rest = _parse_path(variables, path)

    # Read trailing '}'
    if rest[0] != '}':
        # Ill-formed path
        raise Exception("_parse_nested_path(): A nested path has to end with '}}': {}" \
                        .format(path))
    rest = rest[1:]

    return value, rest

def _parse_path(variables, path):
    """Parse a path - which might contain recusive nested paths - and
    return its value.

    """

    # Parse the longest prefix
    # made of any characters beyond '{' and '}'
    path, rest = _parse_path_string(variables, path)

    # Parse any number of 
    # a nested path followed by a path string
    while rest != '' and rest[0] != '}' and rest[0] == '{':
        
        # Parse a nested path
        value, rest = _parse_nested_path(variables, rest)
        path += value
        
        # Parse a path string
        # (A string containing either '{' nor '}')
        string, rest = _parse_path_string(variables, rest)
        path += string

    # Hyphens in paths are converted to underlines
    # Substitute all hyphens ('-') in the path with underlines '_'
    path = path.replace('-', '_')
    
    # Retrive the value of the path
    value = get_recursively(variables, path)

    # DEBUG
    #| print("DEBUG get_recursively(variables, '{}'): {}".format(path, value))

    # Ensure that the file exists
    if value == None:
        print('ERROR Undefined data path: {}'.format(path))
        sys.exit(1)

    return value, rest

def get_path_value(variables, path):
    """Get the value of the given path (which might contain recursive
    nested paths).

    """

    # Get the value of the given path
    value, rest = _parse_path(variables, path)
    
    # Ensure that the whole path has been parsed
    if rest != '':
        # Ill-formed path
        raise Exception("get_path_value(): Ill-formed path: {}" \
                        .format(path))

    return value
       
## =========================================================
## =========================================================

## fin.
