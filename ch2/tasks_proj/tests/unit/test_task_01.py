"""Test the Task data type."""
from tasks import Task


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)

"""
(venv) huzhi@bogon unit % pwd
/Users/huzhi/work/code/pytest_code/ch2/tasks_proj/tests/unit
(venv) huzhi@bogon unit %
(venv) huzhi@bogon unit % pytest -v test_task.py
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.7.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /Users/huzhi/work/code/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/huzhi/work/code/pytest_code/ch2/tasks_proj/tests, inifile: pytest.ini
collected 4 items

test_task.py::test_asdict PASSED                                                                                                                                                                                     [ 25%]
test_task.py::test_replace PASSED                                                                                                                                                                                    [ 50%]
test_task.py::test_defaults PASSED                                                                                                                                                                                   [ 75%]
test_task.py::test_member_access PASSED                                                                                                                                                                              [100%]

==================================================================================================== 4 passed in 0.01s =====================================================================================================
(venv) huzhi@bogon unit %
"""
