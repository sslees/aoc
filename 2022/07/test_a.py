import pytest
from a import solve


def test1():
    assert (
        solve(
            """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
        )
        == 95_437
    )


'''
def test2():
    assert solve("""example2""") == None


def test3():
    assert solve("""example3""") == None
'''

if __name__ == "__main__":
    pytest.main([__file__])
