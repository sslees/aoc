from a import solve
import pytest


def test1():
    assert solve("1122") == 3


def test2():
    assert solve("1111") == 4


def test3():
    assert solve("1234") == 0


def test4():
    assert solve("91212129") == 9


if __name__ == "__main__":
    pytest.main([__file__])
