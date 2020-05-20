"""Test for expected exceptions from using the API wrong."""

import pytest
import tasks

"""
异常处理
"""
def test_add_raises():
    """add() should raise an exception with wrong type param.
    预期发生 TypeError 异常，如果测试通过则说明发生了 TypeError 异常，
    如果测试没有通过，则说明没有发生任何异常，或者发生异常，但不是 TypeError 异常
    """
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception.
    获取异常信息
    """
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


"""
测试标记
pytest -v -m 'get' test_api_exceptions_03.py
pytest -v -m 'smoke' test_api_exceptions_03.py
pytest -v -m 'get and smoke' test_api_exceptions_03.py

and or not
"""
@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


class TestUpdate():
    """Test expected exceptions with tasks.update()."""

    def test_bad_id(self):
        """A non-int id should raise an excption."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1},
                         task=tasks.Task())

    def test_bad_task(self):
        """A non-Task task should raise an excption."""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')


def test_delete_raises():
    """delete() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.delete(task_id=(1, 2, 3))


