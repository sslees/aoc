import pytest
from b import solve


def test_example_1():
    assert solve("1212") == 6


def test_example_2():
    assert solve("1221") == 0


def test_example_3():
    assert solve("123425") == 4


def test_example_4():
    assert solve("123123") == 12


def test_example_5():
    assert solve("12131415") == 4


if __name__ == "__main__":
    pytest.main([__file__])
