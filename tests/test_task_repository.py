from lib.task_repository import TaskRepository
from lib.task import Task
from datetime import date
import pytest


'''
when I call #all_tasks
I get a list of tasks returned
'''
def test_all_tasks_returns_list(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    tasks = repo.all_tasks()
    assert tasks == [
        Task(1, 'Complete Flask web app project', date(2024, 11, 15), tasks[0].date_added, 3, 'pending'),
        Task(1, 'Prepare presentation for project', date(2024, 11, 10), tasks[1].date_added, 2, 'in-progress'),
        Task(2, 'Review portfolio projects', date(2024, 11, 20), tasks[2].date_added, 1, 'pending'),
        Task(2, 'Update resume', date(2024, 11, 12), tasks[3].date_added, 3, 'completed')
    ]
#In future, worth adding in more robust testing for date_added to ensure higher quality. Perhaps a check to ensure timestamp is recent.

'''
given an (task) id
#get_by_task_id returns the Task object with that id
'''
def test_get_by_task_id_gives_task_object(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    task = repo.get_by_task_id(3)
    assert task == Task(2, 'Review portfolio projects', date(2024, 11, 20), task.date_added, 1, 'pending')

'''
Given an (task) id that is not in the DB
#get_by_task raises an error
'''
def test_invalid_task_id_gives_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(IndexError) as e:
        repo.get_by_task_id(100)
    assert str(e.value) == 'No task with id 100 found'

def test_different_invalid_task_id_gives_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(IndexError) as e:
        repo.get_by_task_id(-100)
    assert str(e.value) == 'No task with id -100 found'

def test_again_different_invalid_task_id_gives_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(IndexError) as e:
        repo.get_by_task_id('hi')
    assert str(e.value) == 'No task with id hi found'

'''
given valid parameters 
#add_task puts an extra task in the db
'''
def test_add_task_adds_to_db(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    repo.add_task(2, 'a new task', date(2024, 11, 21), 2, 'in-progress')
    tasks = repo.all_tasks()
    assert tasks == [
        Task(1, 'Complete Flask web app project', date(2024, 11, 15), tasks[0].date_added, 3, 'pending'),
        Task(1, 'Prepare presentation for project', date(2024, 11, 10), tasks[1].date_added, 2, 'in-progress'),
        Task(2, 'Review portfolio projects', date(2024, 11, 20), tasks[2].date_added, 1, 'pending'),
        Task(2, 'Update resume', date(2024, 11, 12), tasks[3].date_added, 3, 'completed'),
        Task(2, 'a new task', date(2024, 11, 21), tasks[4].date_added, 2, 'in-progress')
    ]
