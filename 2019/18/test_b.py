import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """###############
#d.ABC.#.....a#
######@#@######
###############
######@#@######
#b.....#.....c#
###############"""
        )
        == 24
    )


def test_example_2():
    assert (
        solve(
            """#############
#DcBa.#.GhKl#
#.###@#@#I###
#e#d#####j#k#
###C#@#@###J#
#fEbA.#.FgHi#
#############"""
        )
        == 32
    )


def test_example_3():
    assert (
        solve(
            """#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############"""
        )
        == 72
    )


if __name__ == "__main__":
    pytest.main([__file__])
