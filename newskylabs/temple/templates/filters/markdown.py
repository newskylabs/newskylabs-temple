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

"""newskylabs/temple/templates/filters/markdown.py:

A Jinja2 filter for rendering markdown as markdown.

"""

from jinja2 import environmentfilter

#| import re
#| from jinja2 import evalcontextfilter, Markup, escape
#| 
#| _paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
#| 
#| @evalcontextfilter
#| def nl2br(eval_ctx, value):
#|     result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', Markup('<br>\n'))
#|                           for p in _paragraph_re.split(escape(value)))
#|     if eval_ctx.autoescape:
#|         result = Markup(result)
#|     return result

## =========================================================
## jinja tools
## ---------------------------------------------------------

@environmentfilter
def markdown_filter(env, value):
    #| result = do_something(value)
    #| if env.autoescape:
    #|     result = Markup(result)
    #| return result
    #| environmentfilter

    #| marked = md.Markdown(**d)

    try:
        import markdown

    except ImportError:
        log.error(u"Cannot load the markdown library.")
        raise TemplateError(u"Cannot load the markdown library")

    # Markdown extensions to be used
    # 
    # See:
    # 
    #   - Python Markdown Extension
    #     https://python-markdown.github.io/extensions/
    # 
    extensions = [
        #| 'markdown.extensions.attr_list',    # Attribute Lists
        #| 'markdown.extensions.legacy_attr',   # Legacy Attributes
    ]
    #| 
    #| d = dict()
    #| d['extensions'] = list()
    #| d['extensions'].extend(extensions)
    #| 

    md = markdown.Markdown(extensions=extensions)
    #| md = markdown.Markdown(extensions=['markdown'])
    #| out = md.convert(text)

    #| md = markdown.Markdown(**d)
    #str = value.strip()
    marked = md.convert(value)

    return marked

## =========================================================
## =========================================================

## fin.
