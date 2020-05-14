# pants-example-python-multiple-packages
An example repository to demonstrate Python support in Pants v2.

See https://pants.readme.io/ for much more detailed documentation.

# Running Pants

You run Pants goals using the `./pants` wrapper script, which will bootstrap the
configured version of Pants if necessary.

Use `./pants --version` to see the version of Pants configured for the repo (which you can also find
in `pants.toml`).

# Goals

Pants commands are called _goals_. You can get a list of goals with

```
./pants goals
```

# Targets

Targets are sets of source files with some attached metadata. Targets are provided in `BUILD` files.
Targets have types, such as `python_library`, `resources`, `python_binary`. Examples of metadata include
dependencies on other targets, Python version compatibility, entry points for binaries, and so on.

Pants goals can be invoked on targets or directly on source files/directories (which is often more intuitive and convenient).
In the latter case, Pants locates target metadata for the source files as needed.


## Count lines of code

```
./pants cloc '**/*'
```
