from flask import redirect, url_for

def get_index_routes(app):

    @app.route('/', methods=['GET'])
    def get_root_page():
        return redirect(url_for('get_home_page'))