import pytest
from b import solve


def test_example_1():
    assert (
        solve(
            """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
        )
        == None
    )


if __name__ == "__main__":
    pytest.main([__file__])
