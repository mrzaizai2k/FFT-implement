# -*- coding: utf-8 -*-

import pytest
from cooley-tukey-fast-fourier-transform.skeleton import fib

__author__ = "Lisa Burton"
__copyright__ = "Lisa Burton"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
