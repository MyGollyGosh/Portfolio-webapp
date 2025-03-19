from flask import render_template

def get_add_task_routes(app):

    @app.route('/add-task', methods=['GET'])
    def get_add_task():
        return render_template('add_task.html')