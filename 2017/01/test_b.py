from b import main


def test1():
    assert main("1212") == 6


def test2():
    assert main("1221") == 0


def test3():
    assert main("123425") == 4


def test4():
    assert main("123123") == 12


def test5():
    assert main("12131415") == 4
