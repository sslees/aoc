import pytest
from a import solve


def test_example_1():
    assert solve("""16
10
15
5
1
11
7
19
6
12
4""") == None


def test_example_2():
    assert solve("""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""") == None


if __name__ == "__main__":
    pytest.main([__file__])
