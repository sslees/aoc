import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
        )
        == 34
    )


if __name__ == "__main__":
    pytest.main([__file__])
