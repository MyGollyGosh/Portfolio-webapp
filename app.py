import os
from flask import Flask
from flask_login import LoginManager
from lib.user import User
from routes.index import get_index_routes
from routes.home import get_home_routes
from routes.log_in import get_log_in_routes
from routes.sign_up import get_sign_in_routes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'log_in'

@login_manager.user_loader
def load_user():
    try:
        return User.get_id()
    except:
        return None

get_home_routes(app)
get_index_routes(app)
get_log_in_routes(app)
get_sign_in_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))