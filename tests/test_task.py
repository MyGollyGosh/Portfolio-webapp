from lib.task import Task
import pytest

'''
Given a user_id, description, due_date, date_added, priority and status
a Task object is initialised 
'''
def test_task_is_initialised():
    task = Task(2, 'Pass this test', '2024-11-19', '2024-11-18 HH:MI:SS', 1, 'Complete')
    assert task.id == None
    assert task.user_id == 2
    assert task.description == 'Pass this test'
    assert task.due_date == '2024-11-19'
    assert task.date_added == '2024-11-18 HH:MI:SS'
    assert task.priority == 1
    assert task.status == 'Complete'

'''
Given a valid set of parameters except for description
an error is raised
'''
def test_task_init_with_no_description_gives_error():
    with pytest.raises(ValueError) as e:
        Task(2, 'hi', '2024-11-19', '2024-11-18 HH:MI:SS', 1, 'Complete')
    assert str(e.value) == 'Invalid description'

'''
Given a valid set of parameters except not a string for description
an error is raised
'''
def test_description_not_string_gives_error():
    with pytest.raises(TypeError) as e:
        Task(2, 100000, '2024-11-19', '2024-11-18 HH:MI:SS', 1, 'Complete')
    assert str(e.value) == 'Description must be a string'

'''
Given a validf set of parameters except no user_id
an error is raised
'''
def test_no_user_id_gives_error():
    with pytest.raises(TypeError) as e:
        Task(None, 'Pass this test', '2024-11-19', '2024-11-18 HH:MI:SS', 1, 'Complete')
    assert str(e.value) == 'Ensure valid user id (int)'

def test_str_user_id_gives_error():
    with pytest.raises(TypeError) as e:
        Task(None, 'Pass this test', '2024-11-19', '2024-11-18 HH:MI:SS', 1, 'Complete')
    assert str(e.value) == 'Ensure valid user id (int)'

'''
Given valid parameters with invalid user_id
an error is raised
'''
def _test_invalid_user_id_gives_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    with pytest.raises(ValueError) as e:
        Task(3, 'Pass this test', '2024-11-19', '2024-11-18 HH:MI:SS', 1, 'Complete')
    assert str(e.value) == 'No user with id 3 found'


