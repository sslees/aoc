import pytest
from b import solve


def test1():
    assert solve("""mjqjpqmgbljsphdztnvjfqwrcgsmlb""") == 19


def test2():
    assert solve("""bvwbjplbgvbhsrlpgdmjqwftvncz""") == 23


def test3():
    assert solve("""nppdvjthqldpwncqszvftbrmjlhg""") == 23


def test4():
    assert solve("""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""") == 29


def test5():
    assert solve("""zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""") == 26


if __name__ == "__main__":
    pytest.main([__file__])
