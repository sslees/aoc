import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
        )
        == 31
    )


if __name__ == "__main__":
    pytest.main([__file__])
