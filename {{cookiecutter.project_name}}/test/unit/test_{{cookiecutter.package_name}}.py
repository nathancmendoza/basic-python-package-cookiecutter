"""Tests for {{cookiecutter.package_name}}"""

import pytest

def test_vacuous():
    """A test that passes vacuously"""
    pass

def test_exception():
    """A test that checks if an exception was raised"""
    with pytest.raises(ValueError):
        raise ValueError()

@pytest.mark.parametrize("x, y", [(a, b) for a in range(100) for b in range(100)])
def test_parametrize(x y):
    """Test cases can be parametrized to test multiple inputs at once"""
    assert a + b == b + a
