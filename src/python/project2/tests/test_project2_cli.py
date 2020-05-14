from project2.cli import main


def test_cli_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "project1.cli\n3"
