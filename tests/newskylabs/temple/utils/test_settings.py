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
## Tests for Settings.merge_settings()
## ---------------------------------------------------------

from newskylabs.temple.utils.settings import Settings

def test_Settings_merge_settings():

    dic1 = 'whatever'
    dic2 = 'overwrite-setting'
    assert Settings.merge_settings(dic1, dic2) == 'overwrite-setting'

    dic1 = 'whatever'
    dic2 = []
    assert Settings.merge_settings(dic1, dic2) == []

    dic1 = 'whatever'
    dic2 = {}
    assert Settings.merge_settings(dic1, dic2) == {}

    dic1 = 'whatever'
    dic2 = [1, 2, 3]
    assert Settings.merge_settings(dic1, dic2) == [1, 2, 3]

    dic1 = 'whatever'
    dic2 = {'a': 1, 'b': 2, 'c': 3}
    assert Settings.merge_settings(dic1, dic2) == {'a': 1, 'b': 2, 'c': 3}

    dic1 = {'a': 1}
    dic2 = {'b': 2}
    assert Settings.merge_settings(dic1, dic2) == {'a': 1, 'b': 2}

    dic1 = {'a': 'whatever'}
    dic2 = {'a': 'overwrite-setting'}
    assert Settings.merge_settings(dic1, dic2) == {'a': 'overwrite-setting'}

    dic1 = {'a': 1}
    dic2 = {'a': {'b': 2}}
    assert Settings.merge_settings(dic1, dic2) == {'a': {'b': 2}}

    dic1 = {'a': {'b': 2}}
    dic2 = {'a': 1}
    assert Settings.merge_settings(dic1, dic2) == {'a': 1}

    dic1 = {'a': {'b': 1}}
    dic2 = {'c': {'b': 2}}
    assert Settings.merge_settings(dic1, dic2) == {'a': {'b': 1},
                                          'c': {'b': 2}}

    dic1 = {'a': {'b': 1}}
    dic2 = {'a': {'c': 2}}
    assert Settings.merge_settings(dic1, dic2) == {'a': {'b': 1, 'c': 2}}

    dic1 = {'a': {'b': 'whatever'}}
    dic2 = {'a': {'b': 'overwrite-setting'}}
    assert Settings.merge_settings(dic1, dic2) == {'a': {'b': 'overwrite-setting'}}

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
    assert Settings.merge_settings(dic1, dic2) == \
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
## Tests for Settings.merge_settings()
## ---------------------------------------------------------

from newskylabs.temple.utils.settings import Settings

## =========================================================
## Test utilities
## ---------------------------------------------------------

import yaml

def write_settings_file(dic, settings_file):
    with open(settings_file, 'w') as stream:
        yaml.dump(dic, stream)

def cat_settings_file(settings_file):
    print(">>> {}:".format(settings_file))
    with open(settings_file, 'r') as stream:
        print(stream.read())

## =========================================================
## Test fixtures
## ---------------------------------------------------------

@pytest.fixture()
def test_settings1(tmpdir):
    """Create a default settings test file"""

    # Test default settings
    default_settings = {
        'a': 1,
        'c': 1,
        'd': {
            'a': 1,
            'c': 1,
            'd': [1, 2, 3],
        },
    }
    
    # Test user settings
    user_settings = {
        'b': 2,
        'c': 3,
        'd': {
            'b': 2,
            'c': 3,
            'd': [4, 5, 6],
        },
    }
    
    # Create a temporary settings directory
    setting_dir = tmpdir.mkdir(".settings")

    # Write default and user settings to file
    default_settings_file = setting_dir.join("default_settings1.yaml")
    user_settings_file    = setting_dir.join("user_settings1.yaml")

    write_settings_file(default_settings, default_settings_file)
    write_settings_file(user_settings,    user_settings_file)

    return {
        'default-settings':      default_settings, 
        'user-settings':         user_settings,
        'default-settings-file': default_settings_file, 
        'user-settings-file':    user_settings_file,
    }
    
def test_Settings1(test_settings1):

    # ======================================
    # Loading the test fixture
    # --------------------------------------
    default_settings      = test_settings1['default-settings']
    user_settings         = test_settings1['user-settings']
    default_settings_file = test_settings1['default-settings-file']
    user_settings_file    = test_settings1['user-settings-file']

    # DEBUG
    print('DEBUG test_settings1:       ', test_settings1)
    print('DEBUG default_settings:     ', default_settings)
    print('DEBUG user_settings:        ', user_settings)
    print('DEBUG default_settings_file:', default_settings_file)
    print('DEBUG user_settings_file:   ', user_settings_file)
    cat_settings_file(default_settings_file)
    cat_settings_file(user_settings_file)

    # ======================================
    # Tests
    # --------------------------------------
    with pytest.raises(TypeError) as e_info:
        """
        No default settings file given => FileNotFoundError
        """
        default_settings_file2 = None # No file given
        user_settings_file2    = 'some-file'
        settings = Settings(default_settings_file2, user_settings_file2)

    with pytest.raises(FileNotFoundError) as e_info:
        """
        Default settings file not existing => FileNotFoundError
        """
        default_settings_file2 = 'some-non-existing-file'
        user_settings_file2    = 'some-file'
        settings = Settings(default_settings_file2, user_settings_file2)

    settings = Settings(default_settings_file, None)
    assert settings.get_settings() == default_settings
    
    user_settings_file2 = 'some-non-existing-file'
    settings = Settings(default_settings_file, user_settings_file2)
    assert settings.get_settings() == default_settings

    settings = Settings(default_settings_file, user_settings_file)
    assert settings.get_settings() == {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': [4, 5, 6],
        },
    }
    
    for keychain, expected_value in [
            ('undefined', None),
            ('undefined.undefined', None),
            ('a.undefined', None),
            ('a.undefined.undefined', None),
            ('d.undefined', None),
            ('d.undefined.undefined', None),
            ('d.a.undefined', None),
            ('d.a.undefined.undefined', None),
            ('a', 1),
            ('b', 2),
            ('c', 3),
            ('d', {'a': 1, 'b': 2, 'c': 3, 'd': [4, 5, 6]}),
            ('d.a', 1),
            ('d.b', 2),
            ('d.c', 3),
            ('d.d', [4, 5, 6]),
            ('d.d.0', 4),
            ('d.d.1', 5),
            ('d.d.2', 6),
            ('d.d.3', None),
    ]:
        assert settings.get_setting(keychain) == expected_value
    
    settings = Settings(default_settings_file, user_settings_file)
    settings.set_setting('a', 0)
    settings.set_setting('b.b', 2)
    settings.set_setting('c.c.c', 3)
    settings.set_setting('d.a', 0)
    settings.set_setting('d.b.b', 2)
    settings.set_setting('d.c.c.c', 3)
    settings.set_setting('d.d', {'a': 1, 'b': 2, 'c': 3})
    settings.set_setting('d.e', [1, {'e': 1}])
    settings.set_setting('e.e.e.e.e', 5)
    assert settings.get_settings() == {
        'a': 0,
        'b': {'b': 2},
        'c': {'c': {'c': 3}},
        'd': {
            'a': 0,
            'b': {'b': 2},
            'c': {'c': {'c': 3}},
            'd': {'a': 1, 'b': 2, 'c': 3},
            'e': [1, {'e': 1}],
        },
        'e': {'e': {'e': {'e': {'e': 5}}}}
    }

    for keychain, expected_value in [
            ('a', 0),
            ('b.b', 2),
            ('c.c.c', 3),
            ('d', {
                'a': 0,
                'b': {'b': 2},
                'c': {'c': {'c': 3}},
                'd': {'a': 1, 'b': 2, 'c': 3},
                'e': [1, {'e': 1}],
            }),
            ('d.a', 0),
            ('d.b', {'b': 2}),
            ('d.b.b', 2),
            ('d.c', {'c': {'c': 3}}),
            ('d.c.c', {'c': 3}),
            ('d.c.c.c', 3),
            ('d.d', {'a': 1, 'b': 2, 'c': 3}),
            ('d.d.a', 1),
            ('d.d.b', 2),
            ('d.d.c', 3),
            ('d.e', [1, {'e': 1}]),
            ('d.e.0', 1),
            ('d.e.1', {'e': 1}),
            ('d.e.1.e', 1),
            ('e', {'e': {'e': {'e': {'e': 5}}}}),
            ('e.e.e.e.e', 5),
    ]:
        assert settings.get_setting(keychain) == expected_value

## =========================================================
## Test fixtures
## ---------------------------------------------------------

@pytest.fixture()
def test_settings2(tmpdir):
    """Create a default settings test file"""

    # Test default settings
    default_settings = {   

        'author':  {
            'first-name':  'New',
            'family-name': 'Sky',
            'email':       'labs@new.sky',
        },
        
        'company': 'NewSkyLabs',
        'version': '0.0.1.dev1',
        'status':  'Development',
        'license': 'MIT',
        
        'newskylabs-python-project': {
            'language': 'Python',
            'template-dir': '/path/to/templates',
            'project-dir': '.',
        },
    }
    
    # Test user settings
    user_settings = {   

        'author':  {
            'first-name':  'Dietrich',
            'family-name': 'Bollmann',
            'email':       'dietrich@newskylabs.net',
        },
        
        'version': '1.2.3',
        'status':  'Production',
        
        'newskylabs-cpp-project': {
            'language': 'C++',
            'template-dir': '/path/to/cpp-templates',
            'project-dir': '.',
        },
    }
    
    # Create a temporary settings directory
    setting_dir = tmpdir.mkdir(".settings")

    # Write default and user settings to file
    default_settings_file = setting_dir.join("default_settings2.yaml")
    user_settings_file    = setting_dir.join("user_settings2.yaml")

    write_settings_file(default_settings, default_settings_file)
    write_settings_file(user_settings,    user_settings_file)

    return {
        'default-settings':      default_settings, 
        'user-settings':         user_settings,
        'default-settings-file': default_settings_file, 
        'user-settings-file':    user_settings_file,
    }
    
def test_Settings2(test_settings2):

    # ======================================
    # Loading the test fixture
    # --------------------------------------
    default_settings_file = test_settings2['default-settings-file']
    user_settings_file    = test_settings2['user-settings-file']

    # DEBUG
    print('DEBUG default_settings_file:', default_settings_file)
    print('DEBUG user_settings_file:   ', user_settings_file)
    cat_settings_file(default_settings_file)
    cat_settings_file(user_settings_file)

    # ======================================
    # Tests
    # --------------------------------------
    settings = Settings(default_settings_file, user_settings_file)
    for keychain, expected_value in [
            ('author.first-name',                      'Dietrich'),
            ('author.family-name',                     'Bollmann'),
            ('author.email',                           'dietrich@newskylabs.net'),
            ('company',                                'NewSkyLabs'),
            ('version',                                '1.2.3'),
            ('status',                                 'Production'),
            ('license',                                'MIT'),
            ('newskylabs-python-project.language',     'Python'),
            ('newskylabs-python-project.template-dir', '/path/to/templates'),
            ('newskylabs-python-project.project-dir',  '.'),
            ('newskylabs-cpp-project.language',        'C++'),
            ('newskylabs-cpp-project.template-dir',    '/path/to/cpp-templates'),
            ('newskylabs-cpp-project.project-dir',     '.'),
    ]:
        assert settings.get_setting(keychain) == expected_value

## =========================================================
## =========================================================

## fin.
