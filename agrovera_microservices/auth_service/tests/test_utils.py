import pytest
from auth_service import utils

def test_add():
    assert utils.add(2, 3) == 5
    assert utils.add(-1, 1) == 0
    assert utils.add(0, 0) == 0
