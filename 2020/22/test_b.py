import pytest
from b import solve


def test_example_1():
    assert solve("""Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""") == None


def test_example_2():
    assert solve("""Player 1:
43
19

Player 2:
2
29
14""") == None


if __name__ == "__main__":
    pytest.main([__file__])
