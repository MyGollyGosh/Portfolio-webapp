import os
from flask import Flask
from flask_login import LoginManager
#from lib.user import User
from lib.user_repository import UserRepository
from lib.database_connection import get_flask_database_connection
from routes.index import get_index_routes
from routes.home import get_home_routes
from routes.login import get_log_in_routes
from routes.sign_up import get_sign_in_routes
from routes.logout import get_logout_routes
from routes.tasks import get_tasks_routes
from routes.manage_tasks import get_manage_tasks_routes
from routes.add_task import get_add_task_routes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'log_in'

@login_manager.user_loader
def load_user(user_id):
    try:
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        user_id = int(user_id)
        user = repo.get_by_id(user_id)
        if user is None:
            return None
        return user
    except ValueError:
        return None


get_home_routes(app)
get_index_routes(app)
get_log_in_routes(app)
get_sign_in_routes(app)
get_logout_routes(app)
get_tasks_routes(app)
get_manage_tasks_routes(app)
get_add_task_routes(app)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))