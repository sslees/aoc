import pytest
from b import solve


def test1():
    assert solve("""3,4,3,1,2""") == 26_984_457_539


if __name__ == "__main__":
    pytest.main([__file__])
