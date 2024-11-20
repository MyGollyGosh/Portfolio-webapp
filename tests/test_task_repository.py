from lib.task_repository import TaskRepository
from lib.task import Task

'''
when I call #all_tasks
I get a list of tasks returned
'''
def test_all_tasks_returns_list(db_connection):
    db_connection.seed('seeds/task_seeds.sql')
    repo = TaskRepository(db_connection)
    tasks = repo.all_tasks()
    assert tasks == [
        Task(1, 'Complete Flask web app project', '2024-11-15', tasks[0].timestamp, 3, 'pending'),
        Task(1, 'Prepare presentation for project', '2024-11-10', tasks[1].timestamp, 2, 'in-progress'),
        Task(2, 'Review portfolio projects', '2024-11-20', tasks[2].timestap, 1, 'pending'),
        Task((2, 'Update resume', '2024-11-12', tasks[3].timestamp, 3, 'completed'))
    ]