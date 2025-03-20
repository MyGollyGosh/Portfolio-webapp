from flask import render_template, request
from lib.task_repository import TaskRepository
from lib.database_connection import get_flask_database_connection
from flask_login import current_user



def get_manage_tasks_routes(app):

    @app.route('/manage-tasks', methods=['GET', 'POST'])
    def get_manage_tasks_page():
        task_repo = TaskRepository(get_flask_database_connection(app))
        user_tasks = task_repo.get_by_user_id(current_user.id)
        
        selected_task = None
        tasks = []
        
        for task in user_tasks:
            task_details = {
                'description': task.description,
                'due_date': task.due_date,
                'priority': task.priority,
                'status': task.status,
                'date_added': task.date_added,
                'id': task.id
            }
            tasks.append(task_details)
        
        if request.method == 'POST':
            if 'task' in request.form:
                task_id = request.form.get('task')
                if task_id and task_id != 'please select an option':
                    selected_task = task_repo.get_by_task_id(task_id)
        
        return render_template('manage_tasks.html', tasks=tasks, selected_task=selected_task)
