from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository


def get_log_in_routes(app):

    @app.route('/log-in', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('get_home_page'))
        
        if request.method == 'POST':
            connection = get_flask_database_connection(app)
            repo = UserRepository(connection)
            username = request.form['uname']
            password = request.form['pwd']
            is_valid, user = repo.validate_user(username, password)
            if is_valid:
                login_user(user)
                return redirect(url_for('get_home_page'))
            else:
                return render_template('/log_in.html', log_in_message='Invalid username or password')
        
        return render_template('/log_in.html')