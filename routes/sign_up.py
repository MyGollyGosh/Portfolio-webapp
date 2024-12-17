from flask import render_template, request, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository

def get_sign_in_routes(app):

    @app.route('/sign-up', methods=['GET'])
    def get_sign_up_page():
        return render_template('sign_up.html')
    
    @app.route('/sign-up', methods=['POST'])
    def sign_up_user():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        username = request.form['uname']
        email = request.form['email']
        password = request.form['psw']
        if repo.add(username, email, password):
            return redirect('/home')


