


python_library(
    # name defaults to the name of this directory, i.e., `library1`.
    # sources defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
    sources = [
        'src/**/*.py',
    ],
    dependencies = [
    ],
)

python_tests(
    name = 'tests',
    # sources defaults to ['*_test.py', 'test_*.py', 'conftest.py'].
    sources = [
        'tests/**/test_*.py',
        'tests/**/conftest.py',
    ],
    dependencies = [
        ":library1",
    ]
)