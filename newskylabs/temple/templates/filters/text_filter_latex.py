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

"""newskylabs/temple/templates/filters/text_filter_html.py:

A filter for generating html code from the temple xml-based text
representation.

"""

from xml.etree.ElementTree import Element
from newskylabs.temple.templates.filters.nested_paths import get_path_value
from newskylabs.temple.templates.filters.text_filter import TextFilter
from newskylabs.temple.templates.filters.latex_utilities import LaTeXPrinter

## =========================================================
## class TextFilterLaTeX
## ---------------------------------------------------------
        
class TextFilterLaTeX(TextFilter):
    """
    """

    def __init__(self, text, variables):
        super().__init__(text)
        self._variables = variables

    def print(self):
        """
        """
        root = self._root_out
        printer = self.to_string()
        printer.print()
            
    def to_string(self):
        """
        """
        root = self._root_out
        printer = LaTeXPrinter(root, text_tag=self._temple_text_tag)
        return printer.to_string()
            
    def compile_i(self, elem_in):

        # The small cups tags <i>text</i>
        # are rendered as \textit{text}
        elem_out = Element('textit')
        
        # Add leading text, child elements, and trailing text 
        self.add_temple_text_and_child_elements(elem_in, elem_out)

        return elem_out

    def compile_b(self, elem_in):

        # The small cups tags <i>text</i>
        # are rendered as \textit{text}
        elem_out = Element('textbf')
        
        # Add leading text, child elements, and trailing text 
        self.add_temple_text_and_child_elements(elem_in, elem_out)

        return elem_out

    def compile_q(self, elem_in):

        # quotes <q>text</q>
        # are rendered as \quotes{text}
        # which has to be defined as:
        # \newcommand{\quotes}[1]{`#1'}
        elem_out = Element('quotes')

        # Add leading text, child elements, and trailing text 
        self.add_temple_text_and_child_elements(elem_in, elem_out)

        return elem_out

    def compile_sq(self, elem_in):

        # quotes <sq>text</sq>
        # are rendered as \singlequotes{text}
        # which has to be defined as:
        # \newcommand{\singlequotes}[1]{``#1''}
        elem_out = Element('singlequotes')

        # Add leading text, child elements, and trailing text 
        self.add_temple_text_and_child_elements(elem_in, elem_out)

        return elem_out

    def compile_sc(self, elem_in):

        # The small cups tags <sc>text</sc>
        # are rendered as \textsc{text}
        elem_out = Element('textsc')
        
        # Add leading text, child elements, and trailing text 
        self.add_temple_text_and_child_elements(elem_in, elem_out)

        return elem_out

    def compile_em(self, elem_in):

        # The small cups tags <em>text</em>
        # are rendered as \emph{text}
        elem_out = Element('emph')
        
        # Add leading text, child elements, and trailing text 
        self.add_temple_text_and_child_elements(elem_in, elem_out)

        return elem_out

    def compile_strong(self, elem_in):

        # The small cups tags <strong>text</strong>
        # are rendered as \textit{text}
        elem_out = Element('textbf')
        
        # Add leading text, child elements, and trailing text 
        self.add_temple_text_and_child_elements(elem_in, elem_out)

        return elem_out

    def compile_em_dash(self, elem_in):

        # The <em-dash/> is rendered as ---
        elem_out = Element(self._temple_text_tag)
        elem_out.text = '---'
        elem_out.tail = elem_in.tail
        return elem_out

    def compile_temple(self, elem_in):

        # Use a temple <temple_text></temple_text> element:
        # When the text element is converted to text later 
        # the tag is ignored 
        # and only its text, tail and child elements are rendered
        elem_out = Element(self._temple_text_tag)

        # Get the temple variables
        # and the (possibly nexted) path from the <temple /> tag
        # and retrive the corresponding value
        variables = self._variables
        path = elem_in.get('var')
        value = get_path_value(variables, path)

        # Add leading text
        elem_out.text = value

        return elem_out

## =========================================================
## =========================================================

## fin.
