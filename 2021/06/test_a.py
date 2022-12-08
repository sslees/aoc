import pytest
from a import solve


def test_example_1():
    assert solve("""3,4,3,1,2""") == 5_934


if __name__ == "__main__":
    pytest.main([__file__])
