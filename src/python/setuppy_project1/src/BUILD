
python_binary(
    name = 'setuppy1',
    sources = ['setuppy1/cli.py'],
    entry_point = 'setuppy1.cli:main',
    dependencies = [
        ":setuppy1_distribution",
    ],
)


python_library(
    name = 'setuppy1_distribution',
    sources = [
        'setuppy1/**/*.py',
    ],
    dependencies = [
    ],
    provides=setup_py(
        name="setuppy1",
        version="0.0.1",
        description="An example library built with Pants.",
        author="Pantsbuild",
        classifiers=[
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
    ).with_binaries(
        {"my_setuppy1_command": ":setuppy1"},
    ),
)

