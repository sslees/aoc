import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
        )
        == 29
    )


if __name__ == "__main__":
    pytest.main([__file__])
