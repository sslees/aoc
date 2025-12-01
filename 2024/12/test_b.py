import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """AAAA
BBCD
BBCC
EEEC"""
        )
        == 80
    )


def test_example_2():
    assert (
        solve(
            """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
        )
        == 436
    )


def test_example_3():
    assert (
        solve(
            """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
        )
        == 1206
    )


def test_example_4():
    assert (
        solve(
            """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
        )
        == 236
    )


def test_example_5():
    assert (
        solve(
            """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
        )
        == 368
    )


if __name__ == "__main__":
    pytest.main([__file__])
