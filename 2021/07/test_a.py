import pytest
from a import solve


def test1():
    assert solve("""16,1,2,0,4,2,7,1,2,14""") == 37


if __name__ == "__main__":
    pytest.main([__file__])
