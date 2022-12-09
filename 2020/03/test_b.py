import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
        )
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
