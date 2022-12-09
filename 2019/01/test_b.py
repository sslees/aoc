import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """14
1969
100756"""
        )
        == 2 + 966 + 50_346
    )


if __name__ == "__main__":
    pytest.main([__file__])
