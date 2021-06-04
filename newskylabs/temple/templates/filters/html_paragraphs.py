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

"""newskylabs/temple/templates/filters/html_paragraphs.py:

Adds <p></p> tags around paragraphs marked by double newlines.

Example:

In:
============================================================
  
	   		

  
   	  bla bla bla bla bla bla bla bla bla bla bla bla   
		bla bla bla bla bla bla bla bla bla bla bla bla   
   	bla bla bla bla bla bla bla bla bla bla bla bla	

  bla bla bla bla bla bla bla bla bla bla bla bla  	 
          bla bla bla bla bla bla bla bla bla bla bla bla 		
	    bla bla bla bla bla bla bla bla bla bla bla bla		
  


		bla bla bla bla bla bla bla bla bla bla bla bla     
  	  bla bla bla bla bla bla bla bla bla bla bla bla 
   bla bla bla bla bla bla bla bla bla bla bla bla  



------------------------------------------------------------

Out:
============================================================
  <p>
    bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla
  </p>
  <p>
    bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla
  </p>
  <p>
    bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla
  </p>
------------------------------------------------------------
"""
import re

from jinja2 import environmentfilter

## =========================================================
## html_paragraph filter
## ---------------------------------------------------------

@environmentfilter
def html_paragraph_filter(env, text):
    """Adds <p></p> tags around paragraphs marked by double newlines.

    """

    #      "\n  <p>\n  </p>\n    ",

    
    # Remove leading and trailing and whitespace
    text = text.strip()

    # Insert </p><p> for all text paragraphe breaks 
    # (whitspaces containing 2 or more newlines)
    text = re.sub(
           r"[ \t]*\n[ \t]*\n[ \t\n]*",
           "</p><p>",
           text
       )

    # Clean up whitespaces containing one newline
    # for nicer indentation
    text = re.sub(
           r"[ \t]*\n[ \t]*",
           "\n    ",
           text
       )

    # Indent paragraph tags
    text = text.replace('</p><p>', '\n  </p>\n  <p>\n    ')

    # Add paragraph tags at the begin and the end of the text
    text = '  <p>\n    {}\n  </p>'.format(text)

    return text
    
## =========================================================
## =========================================================

## fin.
