import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """12
14
1969
100756"""
        )
        == 2 + 2 + 654 + 33_583
    )


if __name__ == "__main__":
    pytest.main([__file__])
