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
from newskylabs.temple.templates.filters.html_utilities import HTMLPrinter

## =========================================================
## class TextFilterHTML
## ---------------------------------------------------------
        
class TextFilterHTML(TextFilter):
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
        printer = HTMLPrinter(root, text_tag=self._temple_text_tag)
        return printer.to_string()
            
    def compile_sc(self, elem_in):

        # The small cups tags <sc>text</sc>
        # are rendered as <span class="small-cups">text</span>"        
        elem_out = Element('span')
        elem_out.set('class', 'small-cups')
        
        # Add leading text, child elements, and trailing text 
        self.add_temple_text_and_child_elements(elem_in, elem_out)

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

    def compile_em_dash(self, elem_in):
        """<em-dash />"""
        elem_out = Element(self._temple_text_tag)
        elem_out.text = '&mdash;'
        elem_out.tail = elem_in.tail
        return elem_out

    def compile_nbsp(self, elem_in):
        """<nbsp />"""
        elem_out = Element(self._temple_text_tag)
        elem_out.text = '&nbsp;'
        elem_out.tail = elem_in.tail
        return elem_out

    def compile_thinsp(self, elem_in):
        """<thinsp />"""
        elem_out = Element(self._temple_text_tag)
        elem_out.text = '&thinsp;'
        elem_out.tail = elem_in.tail
        return elem_out

    def compile_emsp(self, elem_in):
        """<emsp />"""
        elem_out = Element(self._temple_text_tag)
        elem_out.text = '&emsp;'
        elem_out.tail = elem_in.tail
        return elem_out

    def compile_ensp(self, elem_in):
        """<ensp />"""
        elem_out = Element(self._temple_text_tag)
        elem_out.text = '&ensp;'
        elem_out.tail = elem_in.tail
        return elem_out

## =========================================================
## =========================================================

## fin.
