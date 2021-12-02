from b import solve
import pytest


def test1():
    assert solve("1212") == 6


def test2():
    assert solve("1221") == 0


def test3():
    assert solve("123425") == 4


def test4():
    assert solve("123123") == 12


def test5():
    assert solve("12131415") == 4


if __name__ == "__main__":
    pytest.main([__file__])
