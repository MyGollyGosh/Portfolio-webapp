from flask import render_template, request
from flask_login import current_user
from lib.task_repository import TaskRepository
from lib.database_connection import get_flask_database_connection

def get_add_task_routes(app):

    @app.route('/add-task', methods=['GET', 'POST'])
    def get_add_task():
        print(request.method)
        if request.method == 'GET':
            return render_template('add_task.html')
        
        if request.method == 'POST':
            connection = get_flask_database_connection(app)
            repo = TaskRepository(connection)
            description = request.form['description']
            due_date = request.form['due-date']
            priority = request.form['priority']
            repo.add_task(current_user.id, description, due_date, priority, 'pending')
            print('21')
            print(repo.all_tasks())
            
