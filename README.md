
# newskylabs-temple - [NEWSKYLABS](http://newskylabs.net/) TEMPLatE generator

A tool to generate file trees from template file trees.


## Installation

You can install *temple* with *pip* directly from its *[github repository](https://github.com/newskylabs/newskylabs-temple)*:

```sh
pip install --process-dependency-links git+https://github.com/newskylabs/newskylabs-temple          
```


## Usage

1. Create some templates using the Jinja2 syntax - for example:

```sh
mkdir -p templates/project

cat > templates/project/README <<FIN
This is the README of {{ company.name }}'s {{ project.language }} project {{ project.name }}
FIN

cat > templates/project/about.md <<FIN
# {{ company.name }}'s {{ project.language }} project {{ project.name }}

* project name:  {{ project.name }}
* author:        {{ author.name }}
* email:         {{ author.email }}
* company:       {{ company.name }}
* date:          {{ date }}
* copyright:     {{ copyright }}
FIN

```

For more information concerning the templates see the [homepage of
*Jinja2*](http://jinja.pocoo.org/docs/).


2. Create a *temple* settings file:

```sh
mkdir -p ~/.newskylabs/temple

cat > ~/.newskylabs/temple/settings.yaml <<FIN
## temple's setting file

author:
  first-name: Your
  family-name: Name
  email: your@email.address

company: 
  name: YourCompany

version: 1.0.0
status: Production
license: MIT

cpp-project:
  language: C++
  template-dir: templates
  project-dir: .

FIN

```

3. Use *temple* to generate a file directory tree corresponding to the
template hierarchy:

```sh
temple generate cpp-project my-project
```

4. Have a look on the result:

```sh
$ find my-project
my-project
my-project/my-project.git
my-project/my-project.git/project
my-project/my-project.git/project/README
my-project/my-project.git/project/about.md

$ cat my-project/my-project.git/project/README
This is the README of YourCompany's C++ project my-project

$ cat my-project/my-project.git/project/about.md 
# YourCompany's C++ project my-project

* project name:  my-project
* author:        Your Name
* email:         your@email.address
* company:       YourCompany
* date:          2019/03/04
* copyright:     Copyright 2019 Your Name

```


### Of course, you could also work with predifined templates:

1. Download the templates:

```sh
git clone https://github.com/newskylabs/newskylabs-temple-python
```


2. Create a *temple* settings file:

```sh
mkdir -p ~/.newskylabs/temple

cat > ~/.newskylabs/temple/settings.yaml <<FIN
## temple's setting file

author:
  first-name: Your
  family-name: Name
  email: your@email.address

company: 
  name: YourCompany

version: 1.0.0
status: Production
license: MIT

python-project:
  language: Python
  template-dir: newskylabs-temple-python
  project-dir: .

FIN

```

3. Use *temple* to generate a file directory tree corresponding to the
template hierarchy:

```sh
temple generate python-project my-project
```

4. Have a look on the result:

```sh
$ find my-project
my-project
my-project/my-project.git
my-project/my-project.git/LICENSE
my-project/my-project.git/newskylabs
my-project/my-project.git/newskylabs/temple
my-project/my-project.git/newskylabs/temple/__init__.py
my-project/my-project.git/newskylabs/temple/__about__.py
my-project/my-project.git/README.md
my-project/my-project.git/setup.py
my-project/my-project.git/.gitignore

$ tail -10 my-project/my-project.git/README.md

## Project settings

* project name:  my-project
* author:        Your Name
* email:         your@email.address
* company:       YourCompany
* date:          2019/03/04
* copyright:     Copyright 2019 Your Name

```


# Comments etc.

If you have any comments, [please drop me a message](http://dietrich.newskylabs.net/email)!

*Copyright (c) 2015 [Dietrich Bollmann](http://dietrich.newskylabs.net)*

