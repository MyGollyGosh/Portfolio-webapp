from lib.task import Task

class TaskRepository:
    def __init__(self, connection):
        self._connection = connection

    def all_tasks(self) -> list:
        rows = self._connection.execute('SELECT * FROM tasks;')
        print(type(rows[0]['date_added']))
        return [Task(row['user_id'], row['description'], row['due_date'], row['date_added'], row['priority'], row['status']) for row in rows]
