import pytest
from b import solve


def test1():
    assert (
        solve(
            """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
        )
        == 45000
    )


'''
def test2():
    assert solve("""example2""") == None


def test3():
    assert solve("""example3""") == None
'''

if __name__ == "__main__":
    pytest.main([__file__])
