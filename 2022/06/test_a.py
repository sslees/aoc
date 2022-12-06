import pytest
from a import solve


def test1():
    assert solve("""mjqjpqmgbljsphdztnvjfqwrcgsmlb""") == 7


def test2():
    assert solve("""bvwbjplbgvbhsrlpgdmjqwftvncz""") == 5


def test3():
    assert solve("""nppdvjthqldpwncqszvftbrmjlhg""") == 6


def test4():
    assert solve("""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""") == 10


def test5():
    assert solve("""zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""") == 11


if __name__ == "__main__":
    pytest.main([__file__])
