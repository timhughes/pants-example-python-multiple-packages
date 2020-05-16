from project2.cli import main


def test_cli_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "project2.cli\n"
