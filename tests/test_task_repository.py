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
    with pytest.raises(ValueError) as e:
        repo.get_by_task_id(100)
    assert str(e.value) == 'No task with id 100 found'

def test_different_invalid_task_id_gives_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.get_by_task_id(-100)
    assert str(e.value) == 'No task with id -100 found'

def test_again_different_invalid_task_id_gives_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(ValueError) as e:
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

'''
given an invalid param
an apprioriate error is returned
'''
def test_invalid_user_id_doesnt_add(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.add_task(100, 'a new task', date(2024, 11, 21), 2, 'in-progress')
    assert str(e.value) == 'Invalid user_id: 100'
    tasks = repo.all_tasks()
    assert tasks == [
        Task(1, 'Complete Flask web app project', date(2024, 11, 15), tasks[0].date_added, 3, 'pending'),
        Task(1, 'Prepare presentation for project', date(2024, 11, 10), tasks[1].date_added, 2, 'in-progress'),
        Task(2, 'Review portfolio projects', date(2024, 11, 20), tasks[2].date_added, 1, 'pending'),
        Task(2, 'Update resume', date(2024, 11, 12), tasks[3].date_added, 3, 'completed')
    ]
def test_again_invalid_user_id_doesnt_add(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.add_task(-100, 'a new task', date(2024, 11, 21), 2, 'in-progress')
    assert str(e.value) == 'Invalid user_id: -100'
    tasks = repo.all_tasks()
    assert tasks == [
        Task(1, 'Complete Flask web app project', date(2024, 11, 15), tasks[0].date_added, 3, 'pending'),
        Task(1, 'Prepare presentation for project', date(2024, 11, 10), tasks[1].date_added, 2, 'in-progress'),
        Task(2, 'Review portfolio projects', date(2024, 11, 20), tasks[2].date_added, 1, 'pending'),
        Task(2, 'Update resume', date(2024, 11, 12), tasks[3].date_added, 3, 'completed')
    ]
def test_once_again_invalid_user_id_doesnt_add(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.add_task('-100', 'a new task', date(2024, 11, 21), 2, 'in-progress')
    assert str(e.value) == 'Invalid user_id: -100'
    tasks = repo.all_tasks()
    assert tasks == [
        Task(1, 'Complete Flask web app project', date(2024, 11, 15), tasks[0].date_added, 3, 'pending'),
        Task(1, 'Prepare presentation for project', date(2024, 11, 10), tasks[1].date_added, 2, 'in-progress'),
        Task(2, 'Review portfolio projects', date(2024, 11, 20), tasks[2].date_added, 1, 'pending'),
        Task(2, 'Update resume', date(2024, 11, 12), tasks[3].date_added, 3, 'completed')
    ]
def test_invalid_description_doesnt_add_to_db(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.add_task(1, '', date(2024, 11, 21), 2, 'in-progress')
    assert str(e.value) == 'Please enter a description'


'''
Given a valid (task)id and new parameter
#update_task changes the appropriate details in the DB
'''
def test_update_task_updates_db(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    repo.update_task(1, description='Complete fullstack web app project', due_date = date(2025, 1, 29), priority = 1)
    task = repo.get_by_task_id(1)
    assert task == Task(1, 'Complete fullstack web app project', date(2025, 1, 29), task.date_added, 1, 'pending')
    task2 = repo.get_by_task_id(2)
    assert task2 ==  Task(1, 'Prepare presentation for project', date(2024, 11, 10), task.date_added, 2, 'in-progress')
    
def test_update_task_updates_description(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    repo.update_task(1, description='Complete fullstack web app project',)
    task = repo.get_by_task_id(1)
    assert task == Task(1, 'Complete fullstack web app project', date(2024, 11, 15), task.date_added, 3, 'pending')
    task2 = repo.get_by_task_id(2)
    assert task2 ==  Task(1, 'Prepare presentation for project', date(2024, 11, 10), task.date_added, 2, 'in-progress')

def test_update_task_updates_due_date(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    repo.update_task(1, due_date = date(2025, 1, 29))
    task = repo.get_by_task_id(1)
    assert task == Task(1, 'Complete Flask web app project',  date(2025, 1, 29), task.date_added, 3, 'pending')
    task2 = repo.get_by_task_id(2)
    assert task2 ==  Task(1, 'Prepare presentation for project', date(2024, 11, 10), task.date_added, 2, 'in-progress')

def test_update_task_updates_priority(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    repo.update_task(1, priority = 1)
    task = repo.get_by_task_id(1)
    assert task == Task(1, 'Complete Flask web app project',  date(2024, 11, 15), task.date_added, 1, 'pending')
    task2 = repo.get_by_task_id(2)
    assert task2 ==  Task(1, 'Prepare presentation for project', date(2024, 11, 10), task.date_added, 2, 'in-progress')

def test_update_task_updates_status(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    repo.update_task(1, status = 'in-progress')
    task = repo.get_by_task_id(1)
    assert task == Task(1, 'Complete Flask web app project',  date(2024, 11, 15), task.date_added, 3, 'in-progress')
    task2 = repo.get_by_task_id(2)
    assert task2 ==  Task(1, 'Prepare presentation for project', date(2024, 11, 10), task.date_added, 2, 'in-progress')

'''
Given an invalid (task)id
#update_task returns an error
'''
def test_update_task_with_invalid_id_gives_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.update_task(100, description = 'New')
    assert str(e.value) == 'No task with id 100 found'

'''
Given a valid (task)id and an invalid param
#update_task returns an error
'''
def test_invalid_param_gives_error(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.update_task(2, description = '1')
    assert str(e.value) == 'Invalid description'

'''
given valid params 
#delete_task removes a task from the db
'''
def test_delete_task_removes_from_db(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    repo.delete_task(2)
    tasks = repo.all_tasks()
    assert tasks == [
        Task(1, 'Complete Flask web app project', date(2024, 11, 15), tasks[0].date_added, 3, 'pending'),
        Task(2, 'Review portfolio projects', date(2024, 11, 20), tasks[1].date_added, 1, 'pending'),
        Task(2, 'Update resume', date(2024, 11, 12), tasks[2].date_added, 3, 'completed')
    ]

'''
Given a (task)id that doesn't exist
#delete_tasks returns an error
'''
def test_invalid_id_gives_error_on_delete(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    with pytest.raises(ValueError) as e:
        repo.delete_task(100)
    assert str(e.value) == 'No task with id 100 found'
    tasks = repo.all_tasks()
    assert tasks == [
        Task(1, 'Complete Flask web app project', date(2024, 11, 15), tasks[0].date_added, 3, 'pending'),
        Task(1, 'Prepare presentation for project', date(2024, 11, 10), tasks[1].date_added, 2, 'in-progress'),
        Task(2, 'Review portfolio projects', date(2024, 11, 20), tasks[2].date_added, 1, 'pending'),
        Task(2, 'Update resume', date(2024, 11, 12), tasks[3].date_added, 3, 'completed')
    ]

'''
when I call #get_by_user_id
I get a list of all tasks with that users id
'''

def test_user_by_id_gives_list_of_tasks_with_only_that_user(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    user_1_tasks = repo.get_by_user_id(1)
    assert user_1_tasks == [
        Task(1, 'Complete Flask web app project', date(2024, 11, 15), user_1_tasks[0].date_added, 3, 'pending', 1),
        Task(1, 'Prepare presentation for project', date(2024, 11, 10), user_1_tasks[1].date_added, 2, 'in-progress', 2)
    ]