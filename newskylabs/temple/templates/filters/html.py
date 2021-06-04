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

"""newskylabs/temple/templates/filters/html.py:

A Jinja2 filter for rendering markdown as html.

"""

from jinja2 import environmentfilter
from newskylabs.temple.templates.filters.text_filter_html import TextFilterHTML

## =========================================================
## jinja tools
## ---------------------------------------------------------

@environmentfilter
def html_filter(env, value):

    # Get my variable context
    variables = env.temple['variables']

    # Instantiate the HTML filter
    text_filter = TextFilterHTML(value, variables)

    # Filter the value
    text_filter.compile()

    # Convert the filtert value to a string
    htmlstr = text_filter.to_string()

    # Get rid of hy\-phens
    htmlstr = htmlstr.replace('\-', '')

    # Convert ' --- ' to a em dash
    htmlstr = htmlstr.replace('---', '&mdash;')
    htmlstr = htmlstr.replace('--',  '&ndash;')

    # DEBUG
    #| htmlstr = '!!!!!!!! "{}" -> "{}"\n'.format(value, htmlstr)

    return htmlstr

## =========================================================
## =========================================================

## fin.
