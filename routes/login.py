from flask import render_template, request, redirect
from flask_login import login_user
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository


def get_log_in_routes(app):

    @app.route('/log-in', methods=['GET'])
    def get_log_in_page():
        return render_template('log_in.html')

    @app.route('/log-in', methods=['POST'])
    def log_in_user():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        username = request.form['uname']
        password = request.form['pwd']
        is_valid, user = repo.validate_user(username, password)
        if is_valid:
            login_user(user)
            return redirect('/home')
        else:
            return render_template('/log_in.html', log_in_message='Invalid username or password')