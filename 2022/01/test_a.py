import pytest
from a import solve


def test_example_1():
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
        == 24000
    )


'''
def test_example_2():
    assert solve("""example2""") == None


def test_example_3():
    assert solve("""example3""") == None
'''

if __name__ == "__main__":
    pytest.main([__file__])
