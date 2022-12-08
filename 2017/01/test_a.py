import pytest
from a import solve


def test_example_1():
    assert solve("1122") == 3


def test_example_2():
    assert solve("1111") == 4


def test_example_3():
    assert solve("1234") == 0


def test_example_4():
    assert solve("91212129") == 9


if __name__ == "__main__":
    pytest.main([__file__])
