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

"""newskylabs/temple/templates/filters/latex.py:

A Jinja2 filter for rendering markdown as latex.

"""

from jinja2 import environmentfilter
from newskylabs.temple.templates.filters.text_filter_latex import TextFilterLaTeX

## =========================================================
## jinja tools
## ---------------------------------------------------------

@environmentfilter
def latex_filter(env, value):

    # Get my variable context
    variables = env.temple['variables']

    # Instantiate the LaTeX filter
    text_filter = TextFilterLaTeX(value, variables)

    # Filter the value
    text_filter.compile()

    # Convert the filtert value to a string
    latexstr = text_filter.to_string()

    # DEBUG
    #| latexstr = '!!!!!!!! "{}" -> "{}"\n'.format(value, latexstr)

    return latexstr

## =========================================================
## =========================================================

## fin.
