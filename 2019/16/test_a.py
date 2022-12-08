import pytest
from a import solve


def test_example_1():
    assert solve("""12345678""") == None


def test_example_2():
    assert solve("""80871224585914546619083218645595""") == None


def test_example_3():
    assert solve("""19617804207202209144916044189917""") == None


def test_example_4():
    assert solve("""69317163492948606335995924319873""") == None


if __name__ == "__main__":
    pytest.main([__file__])
