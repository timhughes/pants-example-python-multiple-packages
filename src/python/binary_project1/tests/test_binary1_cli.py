from binary1.cli import main


def test_cli_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "binary1.cli\nlibrary1.maths.add(1, 2)\n3\n"
