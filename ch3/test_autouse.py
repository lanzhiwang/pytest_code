"""Demonstrate autouse fixtures."""

import pytest
import time


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session."""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test durations after each function."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))


def test_1():
    """Simulate long-ish running test."""
    time.sleep(1)


def test_2():
    """Simulate slightly longer test."""
    time.sleep(1.23)

"""
(venv) huzhi@bogon ch3 % pytest -v test_autouse.py
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.7.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /Users/huzhi/work/code/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/huzhi/work/code/pytest_code/ch3
collected 2 items

test_autouse.py::test_1 PASSED                                                                                                                                                                                       [ 50%]
test_autouse.py::test_2 PASSED                                                                                                                                                                                       [100%]

==================================================================================================== 2 passed in 2.25s =====================================================================================================
(venv) huzhi@bogon ch3 %
(venv) huzhi@bogon ch3 %
(venv) huzhi@bogon ch3 % pytest -v -s test_autouse.py
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.7.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /Users/huzhi/work/code/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/huzhi/work/code/pytest_code/ch3
collected 2 items

test_autouse.py::test_1 PASSED
test duration : 1.0 seconds

test_autouse.py::test_2 PASSED
test duration : 1.24 seconds
--
finished : 20 May 18:13:56
-----------------


==================================================================================================== 2 passed in 2.24s =====================================================================================================
(venv) huzhi@bogon ch3 %
"""
