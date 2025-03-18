from flask import render_template, request, redirect, url_for
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
                # Handle task selection
                task_id = request.form.get('task')
                if task_id and task_id != 'please select an option':
                    selected_task = task_repo.get_by_task_id(task_id)
            elif 'description' in request.form:
                # Handle adding a new task
                description = request.form.get('description')
                due_date = request.form.get('due_date')
                priority = request.form.get('priority')
                # Add new task to the database (replace with actual repository logic)
                new_task = {
                    'description': description,
                    'due_date': due_date,
                    'priority': priority,
                    'status': 'Pending',  # Default status
                    'date_added': '2025-01-02'  # Replace with the current date
                }
                task_repo.add_task(current_user.id, new_task['description'], new_task['due_date'], new_task['priority'], new_task['status']) # Assuming your repo has an add_task method
                return redirect(url_for('get_manage_tasks_page'))
        
        return render_template('manage_tasks.html', tasks=tasks, selected_task=selected_task)
