from lib.task import Task
import pytest
from datetime import date, datetime

'''
Given a user_id, description, due_date, date_added, priority and status
a Task object is initialised
'''
def test_task_is_initialised():
    task = Task(2, 'Pass this test', date(2024, 11, 19), datetime(2024,11,18, 11,12,13), 1, 'Complete')
    assert task.id == None
    assert task.user_id == 2
    assert task.description == 'Pass this test'
    assert task.due_date == date(2024, 11, 19)
    assert task.date_added == datetime(2024,11,18, 11,12,13)
    assert task.priority == 1
    assert task.status == 'Complete'

'''
Given a valid set of parameters except for description
an error is raised
'''
def test_task_init_with_no_description_gives_error():
    with pytest.raises(ValueError) as e:
        Task(2, 'hi', date(2024, 11, 19), datetime(2024,11,18, 11,12,13), 1, 'Complete')
    assert str(e.value) == 'Invalid description'

'''
Given a valid set of parameters except not a string for description
an error is raised
'''
def test_description_not_string_gives_error():
    with pytest.raises(TypeError) as e:
        Task(2, 100000, date(2024, 11, 19), datetime(2024,11,18, 11,12,13), 1, 'Complete')
    assert str(e.value) == 'Description must be a string'

'''
Given a valid set of parameters except no user_id
an error is raised
'''
def test_no_user_id_gives_error():
    with pytest.raises(TypeError) as e:
        Task(None, 'Pass this test', date(2024, 11, 19), datetime(2024,11,18, 11,12,13), 1, 'Complete')
    assert str(e.value) == 'Ensure valid user id (int)'

def test_str_user_id_gives_error():
    with pytest.raises(TypeError) as e:
        Task('Hi', 'Pass this test', date(2024, 11, 19), datetime(2024,11,18, 11,12,13), 1, 'Complete')
    assert str(e.value) == 'Ensure valid user id (int)'

'''
Given a valid set of parameters except due date 
an error is raised
'''
def test_incorrect_data_type_for_due_date_gives_error():
    with pytest.raises(TypeError) as e:
        Task(2, 'Pass this test', '2024-11-19', datetime(2024,11,18, 11,12,13), 1, 'Complete')
    assert str(e.value) == 'Ensure valid due_date (date(YYYY, MM, DD))'

'''
Given a valid set of parameters except date added
an error is raised
'''
def test_incorrect_data_type_for_date_added_gives_error():
    with pytest.raises(TypeError) as e:
        Task(2, 'Pass this test', date(2024, 11, 19), 2024-11-19, 1, 'Complete')
    assert str(e.value) == 'Ensure valid date_added (datetime(YYYY,MM,DD, HH,MI,SS))'

'''
Given a valid set of parameters except priority
an error is raised
'''
def test_incorrect_data_type_for_priority_gives_error():
    with pytest.raises(TypeError) as e:
        Task(2, 'Pass this test', date(2024, 11, 19), datetime(2024,11,18, 11,12,13), '1', 'Complete')
    assert str(e.value) == 'Ensure valid priority (int 1-5)'


'''
Given a valid set of parameters except status
an error is raised
'''
def test_incorrect_data_type_for_status_gives_error():
    with pytest.raises(TypeError) as e:
        Task(2, 'Pass this test', date(2024, 11, 19), datetime(2024,11,18, 11,12,13), 1, 1)
    assert str(e.value) == 'Ensure valid status (str)'

'''
test equality
'''
def test_equality():
    task1 = Task(2, 'Pass this test', date(2024, 11, 19), datetime(2024,11,18, 11,12,13), 1, 'Complete')
    task2 = Task(2, 'Pass this test', date(2024, 11, 19), datetime(2024,11,18, 11,12,13), 1, 'Complete')
    assert task1 == task2

'''
test formatting
'''
def test_formatting():
    task = Task(2, 'Pass this test', date(2024, 11, 19), datetime(2024,11,18, 11,12,13), 1, 'Complete')
    assert str(task) == "Task(2, Pass this test, 2024-11-19, 2024-11-18 11:12:13, 1, Complete, None)"
