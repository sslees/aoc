import pytest
from b import solve


def test_example_1():
    assert solve("""16,1,2,0,4,2,7,1,2,14""") == 168


if __name__ == "__main__":
    pytest.main([__file__])
