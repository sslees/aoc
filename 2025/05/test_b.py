import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
        )
        == 14
    )


'''
def test_example_2():
    assert solve("""example2""") == None


def test_example_3():
    assert solve("""example3""") == None
'''

if __name__ == "__main__":
    pytest.main([__file__])
