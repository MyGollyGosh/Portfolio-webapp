import os
from flask import Flask
from routes.index import get_index_routes
from routes.home import get_home_routes
from routes.log_in import get_log_in_routes

app = Flask(__name__)

get_home_routes(app)
get_index_routes(app)
get_log_in_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))