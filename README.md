# TinyCalc

## A quick look at the structure

- `src/tinycalc/` is the package, the folder users will `import`
- `src/` layout keeps us from accidentally importing the local folder instead of the installed package. Without it, tests can pass on the machine and fail for everyone else
- `__init__.py` marks the folder as a package. It also defines the public API, meaning what users get from `import tinycalc`

## What's inside the `pyproject.toml` file?

- `[build-system]` says which tool builds the package. Hatchling is modern and needs no configuration
- `[project]` is the metadata. Only `name` and `version` are strictly required
- `dependencies` lists what users need installed. It's empty because the library only uses plain Python
- `[optional.dependencies.dev]` lists what only us need, such as pytest. Install it with `pip install -e ".[dev]"`

## How does `__init__.py` work?

- `from .operations import ...` lets users write `from tinycalc import add` instead of `from tinycalc.operations import add`
- `__all__` lists the name the package supports
