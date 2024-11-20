from lib.task import Task

class TaskRepository:
    def __init__(self, connection):
        self._connection = connection

    def all_tasks(self) -> list:
        rows = self._connection.execute('SELECT * FROM tasks;')
        return [Task(row['user_id'], row['description'], row['due_date'], row['date_added'], row['priority'], row['status']) for row in rows]
    
    def get_by_task_id(self, id) -> object:
        try:
            task = self._connection.execute('SELECT * FROM tasks WHERE id = %s', (id,))[0]
        except:
            raise IndexError(f'No task with id {id} found')
        else:
            return Task(task['user_id'], task['description'], task['due_date'], task['date_added'], task['priority'], task['status'])
