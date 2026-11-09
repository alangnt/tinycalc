# TinyCalc

## A quick look at the structure

- `src/tinycalc/` is the package, the folder users will `import`
- `src/` layout keeps us from accidentally importing the local folder instead of the installed package. Without it, tests can pass on the machine and fail for everyone else
- `__init__.py` marks the folder as a package. It also defines the public API, meaning what users get from `import tinycalc`
