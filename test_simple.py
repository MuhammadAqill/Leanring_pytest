import pytest
import os

def test_simple_add():
    assert 1 + 1 == 2


@pytest.mark.skip
def test_failing():
    assert 'a' == 'b' # kita mark untuk skip
                      # output akan keluar s
                      # s -> skip

@pytest.mark.skipif(os.name == "posix", reason="Does not run on mac")
def test_skipif_failing():
    assert 'a' == 'b'

@pytest.mark.xfail
def test_x_failing():
    assert 'a' == 'b' # apakah 'a' == 'b' ? tidak
                      # output akan keluar x
                      # x -> fail
                      # bermaksud salah

@pytest.mark.xfail
def test_X_failing():
    assert 'a' == 'a' # apakah 'a' == 'a' ? benar
                      # output akan keluar X
                      # x -> true
                      # bermaksud benar
                      # tetapi kita mark ia untuk salah
                      # dengan ini kita tahu ia benar tetapi kita set ia salah dengan @pytest.mark.xfail

