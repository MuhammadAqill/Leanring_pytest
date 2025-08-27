import pytest

def test_simple_add():
    assert 1 + 1 == 2


def test_failing():
    assert 'a' == 'b'

@pytest.mark.skip
def test_failing():
    assert 'a' == 'b'

