from flask import redirect
from flask_login import logout_user

def get_logout_routes(app):

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect('/log-in')