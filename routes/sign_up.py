from flask import render_template, request, redirect, url_for
from flask_login import current_user
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository

def get_sign_in_routes(app):

    @app.route('/sign-up', methods=['GET', 'POST'])
    def get_sign_up_page():
        if current_user.is_authenticated:
             return redirect(url_for('get_home_page'))
        
        if request.method == 'POST':
            connection = get_flask_database_connection(app)
            repo = UserRepository(connection)
            username = request.form['uname']
            email = request.form['email']
            password = request.form['psw']
            if repo.add(username, email, password):
                return redirect(url_for('get_home_page'))

        return render_template('sign_up.html')