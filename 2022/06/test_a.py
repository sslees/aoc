import pytest
from a import solve


def test_example_1():
    assert solve("""mjqjpqmgbljsphdztnvjfqwrcgsmlb""") == 7


def test_example_2():
    assert solve("""bvwbjplbgvbhsrlpgdmjqwftvncz""") == 5


def test_example_3():
    assert solve("""nppdvjthqldpwncqszvftbrmjlhg""") == 6


def test_example_4():
    assert solve("""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""") == 10


def test_example_5():
    assert solve("""zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""") == 11


if __name__ == "__main__":
    pytest.main([__file__])
