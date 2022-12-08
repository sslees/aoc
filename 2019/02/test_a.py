import pytest
from a import solve


def test_example_1():
    assert solve("""1,0,0,0,99
2,3,0,3,99
2,4,4,5,99,0
1,1,1,4,99,5,6,0,99""") == None


if __name__ == "__main__":
    pytest.main([__file__])
