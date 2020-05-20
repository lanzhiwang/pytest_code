"""Demo fixture scope."""

import pytest


@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""


@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture."""


@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture."""


@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture."""


def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures."""


def test_2(sess_scope, mod_scope, func_scope):
    """Demo is more fun with multiple tests."""

@pytest.mark.usefixtures('class_scope')
class TestSomething():
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, multiple tests are more fun."""

"""
(venv) huzhi@bogon ch3 % pytest -v --setup-show test_scope.py
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.7.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /Users/huzhi/work/code/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/huzhi/work/code/pytest_code/ch3
collected 4 items

test_scope.py::test_1
SETUP    S sess_scope
    SETUP    M mod_scope
        SETUP    F func_scope
        test_scope.py::test_1 (fixtures used: func_scope, mod_scope, sess_scope)PASSED
        TEARDOWN F func_scope
test_scope.py::test_2
        SETUP    F func_scope
        test_scope.py::test_2 (fixtures used: func_scope, mod_scope, sess_scope)PASSED
        TEARDOWN F func_scope
test_scope.py::TestSomething::test_3
      SETUP    C class_scope
        test_scope.py::TestSomething::test_3 (fixtures used: class_scope)PASSED
test_scope.py::TestSomething::test_4
        test_scope.py::TestSomething::test_4 (fixtures used: class_scope)PASSED
      TEARDOWN C class_scope
    TEARDOWN M mod_scope
TEARDOWN S sess_scope

==================================================================================================== 4 passed in 0.01s =====================================================================================================
(venv) huzhi@bogon ch3 %
"""
