from lib.task import *
from lib.user_repository import UserRepository

class TaskRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all_tasks(self) -> list:
        rows = self._connection.execute('SELECT * FROM tasks;')
        return [Task(row['user_id'], row['description'], row['due_date'], row['date_added'], row['priority'], row['status']) for row in rows]
    
    def get_by_task_id(self, id) -> object:
        try:
            task = self._connection.execute('SELECT * FROM tasks WHERE id = %s', (id,))[0]
        except:
            raise ValueError(f'No task with id {id} found')
        else:
            return Task(task['user_id'], task['description'], task['due_date'], task['date_added'], task['priority'], task['status'])
        
    def add_task(self, user_id, description, due_date, priority, status) -> None:
        try:
            user = UserRepository(self._connection)
            user.get_by_id(user_id)
            self._connection.execute(
                '''INSERT INTO tasks (
                    user_id, 
                    description, 
                    due_date, 
                    priority, 
                    status
                ) VALUES (%s, %s, %s, %s, %s)''', 
                [user_id, description, due_date, priority, status]
            )
        except:
            raise ValueError(f'Invalid user_id: {user_id}')
        
    def update_task(self, id, description = None, due_date = None, priority = None, status = None) -> None:
        if description is not None:
            check_valid_description(description)
        if due_date is not None:
            check_valid_due_date(due_date)
        if priority is not None:
            check_valid_priority(priority)
        if status is not None:
            check_valid_status(status)
        try:
            self.get_by_task_id(id)
        except:
            raise ValueError(f'No task with id {id} found')    
        else:
            if description is not None:
                self._connection.execute('UPDATE tasks SET description = %s WHERE id = %s', (description, id))
            if due_date is not None:
                self._connection.execute('UPDATE tasks SET due_date = %s WHERE id = %s', (due_date, id))
            if priority is not None:
                self._connection.execute('UPDATE tasks SET priority = %s WHERE id = %s', (priority, id))
            if status is not None:
                self._connection.execute('UPDATE tasks SET status = %s WHERE id = %s', (status, id))

    def delete_task(self, task_id) -> None:
        try:
            self.get_by_task_id(task_id)
        except:
            raise ValueError(f'No task with id {task_id} found')
        self._connection.execute('DELETE FROM tasks WHERE id = %s', (task_id,))

