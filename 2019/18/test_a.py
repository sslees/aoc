import pytest
from a import solve


def test_example_1():
    assert solve("""#########
#b.A.@.a#
#########""") == None


def test_example_2():
    assert solve("""########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################""") == None


def test_example_3():
    assert solve("""########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################""") == None


def test_example_4():
    assert solve("""#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################""") == None


def test_example_5():
    assert solve("""########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################""") == None


if __name__ == "__main__":
    pytest.main([__file__])
