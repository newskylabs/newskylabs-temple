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

"""newskylabs/temple/templates/filters/text_filter.py:

A base filter class for generating html, latex, or other code from the
temple xml-based text representation.

"""

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

## =========================================================
## Utilities
## ---------------------------------------------------------

def _prefix(indent):
    return ' ' * indent * 2

## =========================================================
## class TextFilter
## ---------------------------------------------------------
        
class TextFilter():
    """
    """

    def __init__(self, text):
        """
        """
        text_tag = 'temple_text'
        self._temple_text_tag = text_tag
        self._root_tag = text_tag
        self._root_start_tag = '<{}>'.format(self._root_tag)
        self._root_end_tag = '</{}>'.format(self._root_tag)

        text = '{}{}{}'.format(self._root_start_tag, text, self._root_end_tag)

        self._root_in = ET.fromstring(text)
        self._root_out = None
            
    def compile(self):
        elem_in = self._root_in

        # Compile
        elem_out = self.compile_tree(elem_in)

        self._root_out = elem_out

    def compile_tree(self, elem_in):

        # Is there a special method to deal with elements of the current type?
        tag = elem_in.tag.replace('-', '_')
        method_name = 'compile_{}'.format(tag)
        if hasattr(self, method_name):

            # There is a special method to deal with elements of the current type.
            # Using it
            #| print('DEBUG Method {}() is defined - using it for rendering...' \
            #|       .format(method_name))
            
            method = getattr(self, method_name)
            elem_out = method(elem_in)
            
        else:

            # There is no special method to deal with elements of the current type.
            # Copy over the element
            #| print('DEBUG Method {}() is NOT defined - using default rendering...' \
            #|     .format(method_name))
        
            elem_out = Element(elem_in.tag, attrib=elem_in.attrib)

            #| attribs = elem.attrib
            #| for key, value in sorted(attribs.items()):
            #|     print(' {}="{}"'.format(key, value), end='')

            #| # Add leading text
            #| self.add_leading_text(elem_in, elem_out)
            #| 
            #| # Add child elements
            #| self.add_child_elements(elem_in, elem_out)
            #| 
            #| # Add trailing text
            #| self.add_trailing_text(elem_in, elem_out)

            # Add leading text, child elements, and trailing text 
            self.add_temple_text_and_child_elements(elem_in, elem_out)

        return elem_out
        
    def add_temple_text_and_child_elements(self, elem_in, elem_out):

        # Add leading text
        self.add_leading_text(elem_in, elem_out)

        # Add child elements
        self.add_child_elements(elem_in, elem_out)

        # Add trailing text
        self.add_trailing_text(elem_in, elem_out)

    def add_leading_text(self, elem_in, elem_out):

        # Add leading text
        elem_out.text = elem_in.text

    def add_child_elements(self, elem_in, elem_out):

        # Add child elements
        for child in elem_in:
            child_elem = self.compile_tree(child)
            elem_out.append(child_elem)
            
    def add_trailing_text(self, elem_in, elem_out):

        # Add trailing text
        elem_out.tail = elem_in.tail

    def dump(self):
        indent = 0
        elem = self._root_in
        self.dump_tree(indent, elem)

    def dump_tree(self, indent, elem):
        self.dump_elem(indent, elem)
        for child in elem:
            self.dump_tree(indent + 2, child)
    
    def dump_elem(self, indent, elem):
        prefix = _prefix(indent)
        print('{}{}.tag: {}'.format(prefix, elem, elem.tag))
        print('{}{}.attrib: {}'.format(prefix, elem, elem.attrib))
        print('{}{}.text: {}'.format(prefix, elem, elem.text))
        print('{}{}.tail: {}'.format(prefix, elem, elem.tail))

## =========================================================
## =========================================================

## fin.
