import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """
        )
        == 3263827
    )


'''
def test_example_2():
    assert solve("""example2""") == None


def test_example_3():
    assert solve("""example3""") == None
'''

if __name__ == "__main__":
    pytest.main([__file__])
