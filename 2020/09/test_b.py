import pytest
from b import solve


def test_example_1():
    assert solve("""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""") == None


if __name__ == "__main__":
    pytest.main([__file__])
