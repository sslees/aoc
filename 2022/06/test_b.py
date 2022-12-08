import pytest
from b import solve


def test_example_1():
    assert solve("""mjqjpqmgbljsphdztnvjfqwrcgsmlb""") == 19


def test_example_2():
    assert solve("""bvwbjplbgvbhsrlpgdmjqwftvncz""") == 23


def test_example_3():
    assert solve("""nppdvjthqldpwncqszvftbrmjlhg""") == 23


def test_example_4():
    assert solve("""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""") == 29


def test_example_5():
    assert solve("""zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""") == 26


if __name__ == "__main__":
    pytest.main([__file__])
