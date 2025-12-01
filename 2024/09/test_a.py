import pytest
from a import solve


def test_example_1():
    assert solve("""2333133121414131402""") == 1928


if __name__ == "__main__":
    pytest.main([__file__])
