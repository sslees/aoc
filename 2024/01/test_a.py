import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """3   4
4   3
2   5
1   3
3   9
3   3"""
        )
        == 11
    )


if __name__ == "__main__":
    pytest.main([__file__])
