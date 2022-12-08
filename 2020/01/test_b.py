import pytest
from b import solve


def test_example_1():
    assert solve("""1721
979
366
299
675
1456""") == None


if __name__ == "__main__":
    pytest.main([__file__])
