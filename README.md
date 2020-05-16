# pants-example-python-multiple-packages
[![Github Actions Pants](https://github.com/timhughes/pants-example-python-multiple-packages/workflows/Pants/badge.svg)](https://github.com/timhughes/pants-example-python-multiple-packages/actions?query=workflow%3APants)
[![Travis Build Status](https://travis-ci.com/timhughes/pants-example-python-multiple-packages.svg?branch=master)](https://travis-ci.com/timhughes/pants-example-python-multiple-packages)

An example repository to demonstrate multi-package monorepo support for Python in Pants v2.
This code is a derivative of https://github.com/pantsbuild/example-python 

See https://pants.readme.io/ for much more detailed documentation.

## Projects

This repository contains 4 projects. These projects are all under `src/python` but you can put them wherever you want 
as long as you update `root_patterns` in `pants.toml`.

`root_patterns` are the roots of the python import namespace.

- `binary_project1`: Binary project with dependency on `library_project1` and uses a `src` directory. You need 2 `BUILD`
  files.
- `binary_project2`: Binary project no dependencies and no `src` directory. This means yo can use a single `BUILD` file.
- `library_project1`: Library project for use by `binary_project1`. This never gets built as an artifact.
- `setuppy_project1`: Python application with entry_point that can be built using setuptools in to a `tar`, `whl`, `egg`
  or whatever else setuptools can create.


## Running Pants

You run Pants goals using the `./pants` wrapper script, which will bootstrap the
configured version of Pants if necessary.

Use `./pants --version` to see the version of Pants configured for the repo (which you can also find
in `pants.toml`).

## Goals

Pants commands are called _goals_. You can get a list of goals with

```
./pants goals
```

## Targets

Targets are sets of source files with some attached metadata. Targets are provided in `BUILD` files.
Targets have types, such as `python_library`, `resources`, `python_binary`. Examples of metadata include
dependencies on other targets, Python version compatibility, entry points for binaries, and so on.

Pants goals can be invoked on targets or directly on source files/directories (which is often more intuitive and convenient).
In the latter case, Pants locates target metadata for the source files as needed.

### File specifications

Invoking goals on files is straightforward, e.g.,

```
./pants test src/python/binary_project1/tests/test_binary1_cli.py
```

You can use globs:

```
./pants lint src/python/binary_project1/**/*.py
```

But note that these will be expanded by your shell, so this is equivalent to having used

```
./pants lint src/python/binary_project1/tests/conftest.py src/python/binary_project1/tests/test_binary1_cli.py
```

If you want Pants itself to expand the globs (which is sometimes necessary), you must quote them in the shell:

```
/pants lint 'src/python/binary_project1/**/*.py'
```

Which will expand the `**` to mean search recursively through all directories from this point.  

### Target specifications

Targets are referenced on the command line using their address, of the form `path/to/dir:name`, e.g.,

```
./pants lint src/python/binary_project1/src:binary1
```

You can omit the target name if it is the same as the immediately enclosing directory name, e.g.,

```
./pants lint src/python/binary_project1/tests
```

You can glob over all targets in a directory with a single trailing `:`, or over all targets in a directory
and all its subdirectories with a double trailing `::`, e.g.,

```
./pants lint src/python/binary_project1::
```

### Globbing semantics

When you glob over files or targets, Pants knows to ignore ones that aren't relevant to the requested goal.
For example, if you run the `test` goal over a set of files that includes non-test files, Pants will just ignore
those, rather than error. So you can safely do things like

```
./pants test ::
```

To run all tests.

In some cases trying to run a goal on multiple files or targets will fail due to conflicts. For example, you cannot
`./pants repl ::` because that could glob over both Python 2 and Python 3 code, so there is
no way to select an interpreter compatible with both both to run the REPL on.


## Example Goals

Try these out in this repo!

### List targets

```
./pants list ::  # All targets.

./pants list 'src/**/*.py'  # Just targets containing Python code. (Note the quotes)
```

### Run linters and formatters

```
./pants lint :: # All targets
./pants fmt src/python/binary_project1/src:binary1  # Just a single target.
./pants fmt src/python/binary_project1::  # All targets below a directory.
./pants fmt 'src/python/binary_project1/**/*.py'  # All python files below a directory (Note the quotes)
```

### Run tests

```
./pants test ::  # Run all tests in the repo.
./pants test src/python/binary_project1/tests:tests  # Run all the tests in this target.
./pants test src/python/binary_project1/tests/test_binary1_cli.py  # Run just the tests in this file.
./pants test src/python/binary_project1/tests/test_binary1_cli.py --pytest-args='-k test_cli_main'  # Run just this one test.
```

### Create a runnable binary

```
./pants binary src/python/binary_project1/src:binary1
./pants binary src/python/binary_project1/src/binary1/cli.py  # This does the same as above.
```

### Run a binary

```
./pants run src/python/binary_project1/src:binary1
./pants run src/python/binary_project1/src/binary1/cli.py  # this works if the module is callable.
```

### Open a REPL

```
./pants repl src/python/binary_project1/src:binary1  # The REPL will have all relevant code and dependencies on its sys.path.
./pants repl --shell=ipython src/python/binary_project1/src:binary1
```

### Run `setup.py` commands

```
./pants setup-py --args="bdist_wheel" src/python/setuppy_project1/src:setuppy1_distribution  # Build a wheel.
```


### Count lines of code

```
./pants cloc '**/*'
```
