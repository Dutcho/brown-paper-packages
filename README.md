# Brown paper packages

Brown paper packages tied up with strings<br>
These are a few of my favorite things:

## Table of Contents

* packages for extra [all](#all-packages)
  * [default](#default)
    * packages for [utils](#utils)
    * packages for [typing](#typing)
  * packages for extra [Excel](#excel)
  * packages for extra [data](#data)
  * packages for extra [web](#web)
  * packages for extra [dev](#dev)

## Installation

### Default

To install default packages in [utils](#utils) and [typing](#typing), use:
> uv add brown-paper-packages

### Specific extras

To install default packages in [utils](#utils), [typing](#typing);
and packages for _specific_ extras (choose from [Excel](#excel), [data](#data), [web](#web), [dev](#dev)), 
use `[extra,...]`:
> uv add brown-paper-packages[extra,...]

### All packages

To install default packages in [utils](#utils), [typing](#typing);
and packages for _all_ extras [Excel](#excel), [data](#data), [web](#web), [dev](#dev), 
use [extra](#specific-extras) `[all]`:
> uv add brown-paper-packages[all]

## Usage

Just use the installed packages directly, e.g. 
> import more_itertools

There's no need for (lengthy and useless) 
~~`import brown_paper_packages`~~.

## Contents

See [pyproject.toml file](./pyproject.toml) for details.

### Utils
* Algorithms
  * [more itertools](https://pypi.org/project/more-itertools/)
* Data structures
  * [sorted containers](https://pypi.org/project/sortedcontainers/)
  * [ordered sets](https://pypi.org/project/orderedsets/)
* Platform access
  * [dot .env](https://pypi.org/project/python-dotenv/)
  * [platform dirs](https://pypi.org/project/platformdirs/)

### Typing
* Additional types
  * [typing extensions](https://pypi.org/project/typing-extensions/)
  * [useful types](https://pypi.org/project/useful-types/)
* Annotations
  * [annotated types](https://pypi.org/project/annotated-types/)
  * [annotated doc](https://pypi.org/project/annotated-doc/)

### Excel

### Data

### Web

### Dev
