import pytest
import tasks
from tasks import Task


def test_count_by_adding_tasks():
    new_task_1 = Task('test task 1')
    new_task_2 = Task('test task 1')
    new_task_3 = Task('test task 1')

    tasks.add(new_task_1)
    tasks.add(new_task_2)
    tasks.add(new_task_3)

    assert tasks.count() == 3


def test_add_4():
    """Slightly different take."""
    task_id = tasks.add(Task('sleep', done=True))
    assert isinstance(tasks.count(), int)


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield  # this is where the testing happens
    tasks.stop_tasks_db()
