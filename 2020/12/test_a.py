import pytest
from a import solve


def test_example_1():
    assert solve("""F10
N3
F7
R90
F11""") == None


if __name__ == "__main__":
    pytest.main([__file__])
