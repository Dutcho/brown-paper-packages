from collections.abc import Iterator


def hello() -> str:
    return "brown-paper-packages: " + ', '. join(imports())


def imports() -> Iterator[str]:
    """Iterate over 'extras', i.e. groups of installed packages."""
    try: import more_itertools, sortedcontainers, orderedsets, dotenv, platformdirs
    except ImportError: pass
    else: yield 'utils'

    try: import typing_extensions, useful_types, annotated_types, annotated_doc
    except ImportError: pass
    else: yield 'typing'

    try: import openpyxl, pyxlsb, lxml, defusedxml
    except ImportError: pass
    else: yield 'excel'

    try: import polars, duckdb, fsspec
    except ImportError: pass
    else: yield 'data'

    try: import requests, bs4, html5lib, flask, fastapi, lxml, defusedxml
    except ImportError: pass
    else: yield 'web'

    try: import mypy, ty
    except ImportError: pass
    else: yield 'dev'


if __name__ == '__main__':
    print(hello())
