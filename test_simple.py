import pytest

def test_simple_add():
    assert 1 + 1 == 2


@pytest.mark.skip
def test_failing():
    assert 'a' == 'b'

