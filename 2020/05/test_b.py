import pytest
from b import solve


def test_example_1():
    assert solve("""BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL""") == None


if __name__ == "__main__":
    pytest.main([__file__])
