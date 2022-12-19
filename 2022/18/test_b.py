import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""
        )
        == 58
    )


if __name__ == "__main__":
    pytest.main([__file__])
