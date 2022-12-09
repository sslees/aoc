import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
        )
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
