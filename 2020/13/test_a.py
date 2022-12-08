import pytest
from a import solve


def test_example_1():
    assert solve("""939
7,13,x,x,59,x,31,19""") == None


if __name__ == "__main__":
    pytest.main([__file__])
