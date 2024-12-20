from flask import render_template

def get_tasks_routes(app):

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        return render_template('tasks.html')