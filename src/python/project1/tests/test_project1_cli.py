from project1.cli import main


def test_cli_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "project1.cli\nlibrary1.maths.add(1, 2)\n3\n"
