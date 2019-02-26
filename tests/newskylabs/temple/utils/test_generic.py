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

"""tests/newskylabs/temple/utils/test_generic.py:

Tests for newskylabs/temple/utils/generic.py

Usage:

pytest tests/newskylabs/utils/test_generic.py

"""

import pytest

## =========================================================
## Tests
## ---------------------------------------------------------

## =========================================================
## Tests for set_recursively()
## ---------------------------------------------------------

from newskylabs.temple.utils.generic import set_recursively

def test_set_recursively():

    structure = {}
    assert structure == {}

    set_recursively(structure, 'foo.bar.baz', 123)
    assert structure == {'foo': {'bar': {'baz': 123}}}

    set_recursively(structure, 'foo.bar.baz', 321)
    assert structure == {'foo': {'bar': {'baz': 321}}}

    set_recursively(structure, 'one', 1)
    assert structure == {'foo': {'bar': {'baz': 321}}, 'one': 1}

    set_recursively(structure, 'one.two', 2)
    assert structure == {'foo': {'bar': {'baz': 321}}, 'one': {'two': 2}}

## =========================================================
## Tests for get_recursively()
## ---------------------------------------------------------

from newskylabs.temple.utils.generic import get_recursively

def test_get_recursively():

    structure = {'foo': {'bar': {'baz': 321}}, 'one': {'two': 2}, 'three': 3}

    assert get_recursively(structure, 'undefined') == None
    assert get_recursively(structure, 'one.two.three') == None

    assert get_recursively(structure, 'three') == 3
    assert get_recursively(structure, 'foo') == {'bar': {'baz': 321}}
    assert get_recursively(structure, 'foo.bar') == {'baz': 321}
    assert get_recursively(structure, 'foo.bar.baz') == 321
    assert get_recursively(structure, 'one') == {'two': 2}
    assert get_recursively(structure, 'one.two') == 2

## =========================================================
## =========================================================

## fin.
