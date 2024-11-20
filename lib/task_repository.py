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
        
    def add_task(self, user_id, description, due_date, priority, status):
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