import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """#######
#a.#Cd#
##@#@##
#######
##@#@##
#cB#Ab#
#######"""
        )
        == None
    )


def test_example_2():
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
        == None
    )


def test_example_3():
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
        == None
    )


def test_example_4():
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
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
