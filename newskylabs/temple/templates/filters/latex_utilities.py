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

"""newskylabs/temple/templates/filters/latex_utilities.py

Printing etrees as html...

"""

from io import StringIO

## =========================================================
## class HTMLPrinter
## ---------------------------------------------------------

class LaTeXPrinter():
    """
    """

    def __init__(self, root, text_tag='temple_text'):
        self._root = root
        self._strbuf = StringIO()
        self._temple_text_tag = text_tag

    def print(self, end=''):

        # Don't print the outer tags
        # They have been added only to be able to parse the text
        # with xml.etree.ElementTree.fromstring()
        print_tags = False 

        string = self.to_string(print_tags=print_tags)
        print(string, end=end)

    def to_string(self, print_tags=True):

        # Don't print the outer tags
        # They have been added only to be able to parse the text
        # with xml.etree.ElementTree.fromstring()
        print_tags = False 

        elem = self._root
        self.tree_to_string(elem, print_tags=print_tags)

        # Retrieve string content
        string = self._strbuf.getvalue()

        # Close string buffer object and discard memory
        # .getvalue() will now raise an exception.
        self._strbuf.close()

        # Return the generated string
        return string

    def _write(self, string):
        self._strbuf.write(string)

    def tree_to_string(self, elem, print_tags=True):

        # Only the text content of the text tag 
        #   <temple_text>text</temple_text>
        # is supposed to be printed
        if elem.tag == self._temple_text_tag:
            print_tags = False

        text = elem.text if elem.text else ''
        tail = elem.tail if elem.tail else ''
        has_text = len(text) > 0
        has_elems = len(elem) > 0
        is_empty = not has_text and not has_elems

        # Print start tag
        if print_tags:
            self.start_tag_to_string(elem, is_empty)

        # Print text
        self._write(text)
            
        # Print child elements
        for child in elem:
            self.tree_to_string(child)

        # Print end tag
        if print_tags:
            self.end_tag_to_string(elem, is_empty)

        # Print tail
        self._write(tail)
            
    def start_tag_to_string(self, elem, is_empty):

        self._write('\\{}{{'.format(elem.tag))
        self.attribs_to_string(elem)

    def attribs_to_string(self, elem):
        for key, value in sorted(elem.attrib.items()):
            self._write(' {}="{}"'.format(key, value))

    def end_tag_to_string(self, elem, is_empty):
        if not is_empty:
            self._write('}')

## =========================================================
## =========================================================

## fin.
