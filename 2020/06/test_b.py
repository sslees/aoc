import pytest
from b import solve


def test_example_1():
    assert solve("""abc

a
b
c

ab
ac

a
a
a
a

b""") == None


if __name__ == "__main__":
    pytest.main([__file__])
