# Brown paper packages
Collection of PyPI **packages** to stop repeating myself.

## Background
### Situation
I noted I came back to repetitively installing the same PyPI packages in various projects.
Sometimes, I couldn't recall their name or extras.
At other times, I forgot importing optional, but important (to safety -e.g. `defusedxml`- or performance) dependencies. 

Now, I decided to put in the effort to come [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

### Name
Obviously, this package's name comes
from the <cite>[Sound of Music](https://en.wikipedia.org/wiki/The_Sound_of_Music)</cite> 
song <cite>[My Favorite Things](https://en.wikipedia.org/wiki/My_Favorite_Things_(song))</cite>:
<blockquote>
Brown paper packages tied up with strings<br>
These are a few of my favorite things
</blockquote>
<img src="https://live.staticflickr.com/5012/5560753633_5a03c9cdec_b.jpg" alt="Brown paper packages" height="250"/>

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

This package doesn't contain any functionality of its own.
Therefore, there's no need for (lengthy and useless) 
~~`import brown_paper_packages`~~.

For reuse of classes and functions, see companion [PyPI package raindrops-on-roses](https://pypi.org/project/raindrops-on-roses/).

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
