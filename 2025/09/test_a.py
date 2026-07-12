import pytest
from a import solve


def test_example_1():
    assert (
        solve(
            """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
        )
        == 50
    )


'''
def test_example_2():
    assert solve("""example2""") == None


def test_example_3():
    assert solve("""example3""") == None
'''

if __name__ == "__main__":
    pytest.main([__file__])
