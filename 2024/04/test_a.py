import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
        )
        == 18
    )


if __name__ == "__main__":
    pytest.main([__file__])
