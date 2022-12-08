import pytest
from b import solve


def test_example_1():
    assert solve("""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""") == None


if __name__ == "__main__":
    pytest.main([__file__])
