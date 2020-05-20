def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

"""
(venv) huzhi@bogon ch1 % pytest test_one.py
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.7.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: /Users/huzhi/work/code/pytest_code/ch1
collected 1 item

test_one.py .                                                                                                                                                                                                        [100%]

==================================================================================================== 1 passed in 0.01s =====================================================================================================
(venv) huzhi@bogon ch1 %
(venv) huzhi@bogon ch1 % pytest -v test_one.py
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.7.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /Users/huzhi/work/code/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/huzhi/work/code/pytest_code/ch1
collected 1 item

test_one.py::test_passing PASSED                                                                                                                                                                                     [100%]

==================================================================================================== 1 passed in 0.00s =====================================================================================================
(venv) huzhi@bogon ch1 %
"""
