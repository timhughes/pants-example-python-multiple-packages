from setuppy1.cli import main


def test_cli_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "setuppy1.cli\nsetuppy1.words.join(Hello, World!)\nHello World!\n"
