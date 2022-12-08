import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        )
        == 2
    )


if __name__ == "__main__":
    pytest.main([__file__])
