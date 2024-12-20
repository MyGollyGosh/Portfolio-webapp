from flask import render_template, redirect
from flask_login import current_user

def get_tasks_routes(app):

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        if not current_user.is_authenticated:
            return redirect('/log-in')
        return render_template('tasks.html')
        