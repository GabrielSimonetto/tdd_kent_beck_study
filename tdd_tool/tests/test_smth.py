import pytest

from tdd_tool import WasRun

def test_was_run():
    test = WasRun("test_method")
    assert not test.was_run

    test.run()
    assert test.was_run


