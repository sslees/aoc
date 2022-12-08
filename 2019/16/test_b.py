import pytest
from b import solve


def test_example_1():
    assert solve("""03036732577212944063491565474664""") == None


def test_example_2():
    assert solve("""02935109699940807407585447034323""") == None


def test_example_3():
    assert solve("""03081770884921959731165446850517""") == None


if __name__ == "__main__":
    pytest.main([__file__])
