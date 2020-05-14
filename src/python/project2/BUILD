


python_binary(
    sources = ['src/project2/cli.py'],
    entry_point = 'project2.cli',
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
        ":project2",
    ]
)