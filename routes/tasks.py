from flask import render_template, redirect
from flask_login import current_user
from lib.task_repository import TaskRepository
from lib.database_connection import get_flask_database_connection


def get_tasks_routes(app):

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        if not current_user.is_authenticated:
            return redirect('/log-in')
        
        task_repo = TaskRepository(get_flask_database_connection(app))
        user_tasks = task_repo.get_by_user_id(current_user.id)
        tasks = []
        for task in user_tasks:
            task_details = {
                'description': task.description,
                'due_date': task.due_date,
                'priority': task.priority,
                'status': task.status,
                'date_added': task.date_added
            }
            tasks.append(task_details)


        return render_template('tasks.html', tasks=tasks)
        