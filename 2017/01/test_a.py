from a import main


def test1():
    assert main("1122") == 3


def test2():
    assert main("1111") == 4


def test3():
    assert main("1234") == 0


def test4():
    assert main("91212129") == 9
