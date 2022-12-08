import pytest
from a import solve


def test_example_1():
    assert solve("""0,3,6""") == None


if __name__ == "__main__":
    pytest.main([__file__])
