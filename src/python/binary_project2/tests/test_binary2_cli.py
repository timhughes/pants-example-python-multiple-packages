from binary2.cli import main


def test_cli_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "binary2.cli\n"
