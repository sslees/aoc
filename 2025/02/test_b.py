import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
        )
        == 4174379265
    )


'''
def test_example_2():
    assert solve("""example2""") == None


def test_example_3():
    assert solve("""example3""") == None
'''

if __name__ == "__main__":
    pytest.main([__file__])
