from setuppy1.words import join


def test_words_add():
    assert join("Hello", "World!") == "Hello World!"
