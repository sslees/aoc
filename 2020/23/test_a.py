import pytest
from a import solve


def test_example_1():
    assert solve("""389125467""") == None


if __name__ == "__main__":
    pytest.main([__file__])
