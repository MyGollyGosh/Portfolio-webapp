from flask import render_template, request, redirect
from flask_login import current_user
from lib.task_repository import TaskRepository
from lib.database_connection import get_flask_database_connection
from datetime import datetime

def get_add_task_routes(app):

    @app.route('/add-task', methods=['GET', 'POST'])
    def get_add_task():
        error_message = False
        if request.method == 'GET':
            return render_template('add_task.html', error_message=error_message)
        
        if request.method == 'POST':
            connection = get_flask_database_connection(app)
            repo = TaskRepository(connection)
            description = request.form.get('description')
            due_date_str = request.form.get('due-date')
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except:
                return 'Please stop messing with my website'
            priority = int(request.form.get('priority'))
            if description and due_date and priority:
                repo.add_task(current_user.id, description, due_date, priority, 'pending')
            else:
                error_message = True

            return redirect('/manage-tasks')
            
