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

"""tests/newskylabs/temple/utils/test_settings.py:

Tests for newskylabs/temple/utils/settings.py

Usage:

pytest tests/newskylabs/temple/utils/test_settings.py

"""

import pytest

## =========================================================
## Tests for unify()
## ---------------------------------------------------------

from newskylabs.temple.utils.generic import merge_settings

def test_merge_settings():

    dic1 = 'whatever'
    dic2 = 'overwrite-setting'
    assert merge_settings(dic1, dic2) == 'overwrite-setting'

    dic1 = 'whatever'
    dic2 = []
    assert merge_settings(dic1, dic2) == []

    dic1 = 'whatever'
    dic2 = {}
    assert merge_settings(dic1, dic2) == {}

    dic1 = 'whatever'
    dic2 = [1, 2, 3]
    assert merge_settings(dic1, dic2) == [1, 2, 3]

    dic1 = 'whatever'
    dic2 = {'a': 1, 'b': 2, 'c': 3}
    assert merge_settings(dic1, dic2) == {'a': 1, 'b': 2, 'c': 3}

    dic1 = {'a': 1}
    dic2 = {'b': 2}
    assert merge_settings(dic1, dic2) == {'a': 1, 'b': 2}

    dic1 = {'a': 'whatever'}
    dic2 = {'a': 'overwrite-setting'}
    assert merge_settings(dic1, dic2) == {'a': 'overwrite-setting'}

    dic1 = {'a': 1}
    dic2 = {'a': {'b': 2}}
    assert merge_settings(dic1, dic2) == {'a': {'b': 2}}

    dic1 = {'a': {'b': 2}}
    dic2 = {'a': 1}
    assert merge_settings(dic1, dic2) == {'a': 1}

    dic1 = {'a': {'b': 1}}
    dic2 = {'c': {'b': 2}}
    assert merge_settings(dic1, dic2) == {'a': {'b': 1},
                                          'c': {'b': 2}}

    dic1 = {'a': {'b': 1}}
    dic2 = {'a': {'c': 2}}
    assert merge_settings(dic1, dic2) == {'a': {'b': 1, 'c': 2}}

    dic1 = {'a': {'b': 'whatever'}}
    dic2 = {'a': {'b': 'overwrite-setting'}}
    assert merge_settings(dic1, dic2) == {'a': {'b': 'overwrite-setting'}}

    dic1 = {'a': 1,
            'c': 1,
            'd': 1,
            'e': {'ea': 1},
            'f': {'fa': 1},
            'g': {'ga': 1,
                  'gc': 1, 
                  'gd': 1,
                  'ge': {'gea': 1},
                  'gf': {'gfa': 1},
                  'gg': {'gga': 1,
                         'ggc': 1,
                         'ggd': 1,
                         'gge': {'ggea': 1},
                         'ggf': {'ggfa': 1},
                  },
            },
    }
    
    dic2 = {'b': 2,
            'c': 3,
            'd': {'da': 4},
            'e': 5,
            'f': {'fa': 6},
            'g': {'gb': 2,
                  'gc': 3,
                  'gd': {'gda': 4},
                  'ge': 5,
                  'gf': {'gfa': 6},
                  'gg': {'ggb': 2,
                         'ggc': 3,
                         'ggd': {'ggda': 4},
                         'gge': 5,
                         'ggf': {'ggfa': 6},
                  },
            },
    }
    assert merge_settings(dic1, dic2) == \
        {'a': 1,
         'b': 2,
         'c': 3,
         'd': {'da': 4},
         'e': 5,
         'f': {'fa': 6},
         'g': {'ga': 1,
               'gb': 2,
               'gc': 3, 
               'gd': {'gda': 4},
               'ge': 5,
               'gf': {'gfa': 6},
               'gg': {'gga': 1,
                      'ggb': 2,
                      'ggc': 3,
                      'ggd': {'ggda': 4},
                      'gge': 5,
                      'ggf': {'ggfa': 6},
               },
         },
        }

## =========================================================
## =========================================================

## fin.
